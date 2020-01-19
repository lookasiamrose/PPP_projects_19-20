from django.shortcuts import render
from .forms import LoginForm, OfferForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from .models import Currency
from .models import Offer
from .models import Wallet


def index(request):
    markets = Currency.objects.all()
    offers = Offer.objects.filter(status='OPEN')
    closed = Offer.objects.filter(status='CLOSED').order_by('-time')

    if request.user == None or not request.user.is_authenticated:
        wallets = []
    else:
        wallets = Wallet.objects.filter(userid=request.user)

    compound = []
    for market in markets:
        off = offers.filter(currencyid=market.id)
        if wallets == []:
            wallet = []
            compound.append({"shortname" : market.shortname, "name" : market.name, "wallet" : wallet, "closed" : closed.filter(currencyid=market.id),
            "offers" : { "buys" : off.filter(type='BUY'), "sells" : off.filter(type='SELL') }
            })
        else:
            wallet = wallets.get(currencyid=market.id)
            compound.append({"shortname" : market.shortname, "name" : market.name, "wallet" : wallet.funds, "closed" : closed.filter(currencyid=market.id),
            "offers" : { "buys" : off.filter(type='BUY'), "sells" : off.filter(type='SELL') }
            })


    addOffer = OfferForm()

    return render(request,'index.html', {'compound' : compound, 'addOffer' : addOffer, 'closed' : closed })
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print('The account has issues...')
                    
            else:
                print('The username or password is incorrect!')
                
    #else:
        
    form = LoginForm()
    return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def dashboard(request, username):
    user = User.objects.get(username=username)
    wallets = Wallet.objects.filter(userid=user)
    return render(request, 'dashboard.html',{'username': username,'wallets': wallets})

def market(request, market):
    market = Currency.objects.get(name=market)
    offers = Offer.objects.filter(currencyid=market).filter(status='OPEN')
    closed = Offer.objects.filter(currencyid=market).filter(status='CLOSED').order_by('-time')
    return render(request, 'market.html',{'market': market, 'closed' : closed,'offers' : { "buys" : offers.filter(type='BUY'), "sells" : offers.filter(type='SELL') }})

def access_offer(request):
    offer_id = request.POST.get('offer_id', None)
    if (offer_id):
        offer = Offer.objects.get(id=int(offer_id))
        if offer is not None:
            wallet = Wallet.objects.get(userid=request.user,currencyid=offer.currencyid)
            BTC = Currency.objects.get(shortname='BTC')
            walletBTC = Wallet.objects.get(userid=request.user,currencyid=BTC)

            potential = offer.quantity * offer.ratetobtc
            if offer.type == Offer.Type.BUY:
                if walletBTC.funds > potential:
                    wallet.funds = wallet.funds + offer.quantity
                    #offer.delete()
                    offer.status = Offer.Status.CLOSED
                    offer.save()
                    wallet.save()
                    return HttpResponse(0)
                else:
                    return HttpResponse(4)

            elif offer.type == Offer.Type.SELL: 
                if wallet.funds > offer.quantity:
                    walletBTC.funds = walletBTC.funds + potential        
                    #offer.delete()
                    offer.status = Offer.Status.CLOSED
                    offer.save()
                    walletBTC.save()
                    return HttpResponse(0)
                else:
                    return HttpResponse(4)

            else:
                return HttpResponse(3)

        return HttpResponse(2)

    return HttpResponse(1)

def add_offer(request):
    form = OfferForm(request.POST)
    if form.is_valid():
        offer = form.save(commit = False)
        potential = offer.quantity * offer.ratetobtc

        if offer.type == Offer.Type.BUY:
            wallet = Wallet.objects.get(userid=request.user,currencyid=Currency.objects.get(shortname='BTC'))

            if wallet.funds >= potential:
                wallet.funds = wallet.funds - potential
                wallet.save()
                otherOffers = Offer.objects.filter(currencyid=offer.currencyid,type=Offer.Type.SELL).order_by('ratetobtc')
                for other in otherOffers:
                    potentialI = offer.quantity * offer.ratetobtc
                    if other.ratetobtc <= offer.ratetobtc:
                        otherPotential = other.ratetobtc*other.quantity
                        if otherPotential <= potentialI:
                            offer.quantity = offer.quantity - other.quantity

                            other.status = Offer.Status.CLOSED
                            other.save()
                            offer.save()
                        else:
                            otherQty = potentialI/other.ratetobtc
                            other.quantity = other.quantity - otherQty
                            offer.quantity = 0

                            offer.save()
                            other.save()
                            break
                    else:
                        break


        elif offer.type == Offer.Type.SELL:
            wallet = Wallet.objects.get(userid=request.user,currencyid=offer.currencyid)

            if wallet.funds >= offer.quantity:
                wallet.funds = wallet.funds - offer.quantity
                wallet.save()
                otherOffers = Offer.objects.filter(currencyid=offer.currencyid,type=Offer.Type.BUY).order_by('-ratetobtc')
                for other in otherOffers:
                    potentialI = offer.quantity * offer.ratetobtc
                    if other.ratetobtc >= offer.ratetobtc:
                        otherPotential = other.ratetobtc*other.quantity
                        if otherPotential <= potentialI:
                            offer.quantity = offer.quantity - other.quantity

                            other.status = Offer.Status.CLOSED
                            offer.save()
                            other.save()
                        else:
                            otherQty = potentialI/other.ratetobtc
                            other.quantity = other.quantity - otherQty
                            offer.quantity = 0
                            offer.save()
                            other.save()
                            break
                    else:
                        break
        else:
            return HttpResponseRedirect('/')

        wallet.save()

        offer.userid = request.user
        if offer.quantity > 0:
            offer.status = Offer.Status.OPEN
        else:
            offer.status = Offer.Status.CLOSED
        offer.save()

    return HttpResponseRedirect('/')