import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

#from main_app.models import User
from main_app.models import Currency
from main_app.models import Wallet
from main_app.models import Offer
from django.contrib.auth.models import User

def addUserIfNoE(username, email):
    try:
        u1 = User.objects.get(username=username)
    except:
        u1 = User.objects.create_user(username=username,email=email,password='none')
        u1.save()

def addCurrencyIfNoE(shortname, name):
    try:
        c1 = Currency.objects.get(shortname=shortname)
    except:
        c1 = Currency(shortname=shortname,name=name,logopath='none')
        c1.save()
        
def addWalletIfNoE(userid, currencyid, address, funds):
    try:
        w1 = Wallet.objects.filter(currencyid=currencyid).get(userid=userid)
    except:
        w1 = Wallet(userid=userid,currencyid=currencyid,address=address,funds=funds)
        w1.save()

def addOfferIfNoE(userid, currencyid, type, ratetobtc, quantity, status):
    try:
        o1 = Offer.objects.filter(currencyid=currencyid).get(userid=userid)
    except:
        o1 = Offer(userid=userid, currencyid=currencyid, type=type, ratetobtc=ratetobtc, quantity=quantity, status=status)
        o1.save()
        
if __name__ == '__main__': 
    
    addUserIfNoE(username='Guillotine',email='gulliotinecut@gmail.com')
    addUserIfNoE(username='Johnny',email='johnny.box@example.com')  
    addUserIfNoE(username='Emily',email='emily.box@example.com')
    addUserIfNoE(username='Vladimir',email='vladimir.box@example.com')
    addUserIfNoE(username='Genji',email='genji.box@example.com')
    addUserIfNoE(username='Stefan',email='stefan.box@example.com')
    addUserIfNoE(username='Heniu',email='siemaeniu.box@example.com')
    
    addCurrencyIfNoE(shortname='BTC',name='Bitcoin')
    addCurrencyIfNoE(shortname='LTC',name='Litecoin')
    addCurrencyIfNoE(shortname='XMR',name='Monero')
    addCurrencyIfNoE(shortname='ZEC',name='Zcash')
    addCurrencyIfNoE(shortname='PLN',name='Polish zloty')
    
    addWalletIfNoE(User.objects.get(username='Guillotine'),Currency.objects.get(shortname='BTC'),
                    address='3DE1gRqwehFcgF39Yfq78LnSXmGKMmY3Pv',funds=0.5)
    addWalletIfNoE(User.objects.get(username='Johnny'),Currency.objects.get(shortname='BTC'),
                    address='37SpDxRgvc1RVRhcF1BbmemMU6b5fn2jEc',funds=0.1)
    addWalletIfNoE(User.objects.get(username='Emily'),Currency.objects.get(shortname='BTC'),
                    address='3APNaz8LzVN7DeBCxaqqDTZdUJCQh3qKAk',funds=0.002)
    addWalletIfNoE(User.objects.get(username='Stefan'),Currency.objects.get(shortname='BTC'),
                    address='3APNaz8LzVN7DeBCxaqqDTZdUJCQh3qKA1',funds=0)
    addWalletIfNoE(User.objects.get(username='Heniu'),Currency.objects.get(shortname='BTC'),
                    address='3APNaz8LzVN7DeBCxaqqDTZdUJCQh3qKA2',funds=0)
    addWalletIfNoE(User.objects.get(username='Vladimir'),Currency.objects.get(shortname='BTC'),
                    address='3APNaz8LzVN7DeBCxaqqDTZdUJCQh3qKA3',funds=0)        

    addWalletIfNoE(User.objects.get(username='Guillotine'),Currency.objects.get(shortname='PLN'),
                    address='',funds=0)
    addWalletIfNoE(User.objects.get(username='Johnny'),Currency.objects.get(shortname='PLN'),
                    address='',funds=0)
    addWalletIfNoE(User.objects.get(username='Emily'),Currency.objects.get(shortname='PLN'),
                    address='',funds=0)
    addWalletIfNoE(User.objects.get(username='Stefan'),Currency.objects.get(shortname='PLN'),
                    address='',funds=0)
    addWalletIfNoE(User.objects.get(username='Heniu'),Currency.objects.get(shortname='PLN'),
                    address='',funds=0)
    addWalletIfNoE(User.objects.get(username='Vladimir'),Currency.objects.get(shortname='PLN'),
                    address='',funds=0)
   
    addWalletIfNoE(User.objects.get(username='Guillotine'),Currency.objects.get(shortname='LTC'),
                    address='LPvngjim95xLutFpFri1T8SFGdmUrAjxp9',funds=100)                
    addWalletIfNoE(User.objects.get(username='Johnny'),Currency.objects.get(shortname='LTC'),
                    address='LPvngjim95xLutFpFri1T8SFGdmUrAjxpA',funds=24)      
    addWalletIfNoE(User.objects.get(username='Emily'),Currency.objects.get(shortname='LTC'),
                    address='LPvngjim95xLutFpFri1T8SFGdmUrAjxpB',funds=50)      
    addWalletIfNoE(User.objects.get(username='Stefan'),Currency.objects.get(shortname='LTC'),
                    address='LPvngjim95xLutFpFri1T8SFGdmUrAjxpC',funds=0.323)      
    addWalletIfNoE(User.objects.get(username='Heniu'),Currency.objects.get(shortname='LTC'),
                    address='LPvngjim95xLutFpFri1T8SFGdmUrAjxpD',funds=0.022)      
    
    addWalletIfNoE(User.objects.get(username='Guillotine'),Currency.objects.get(shortname='ZEC'),
                    address='t1MLeN1Us9kSwEN5EvxxqNQDx3kUpKCcPfa',funds=10)                
    addWalletIfNoE(User.objects.get(username='Johnny'),Currency.objects.get(shortname='ZEC'),
                    address='t1MLeN1Us9kSwEN5EvxxqNQDx3kUpKCcPfB',funds=0.03)      
    addWalletIfNoE(User.objects.get(username='Emily'),Currency.objects.get(shortname='ZEC'),
                    address='t1MLeN1Us9kSwEN5EvxxqNQDx3kUpKCcPfC',funds=0.75)      
    addWalletIfNoE(User.objects.get(username='Stefan'),Currency.objects.get(shortname='ZEC'),
                    address='t1MLeN1Us9kSwEN5EvxxqNQDx3kUpKCcPfD',funds=1.1)      
    addWalletIfNoE(User.objects.get(username='Heniu'),Currency.objects.get(shortname='ZEC'),
                    address='t1MLeN1Us9kSwEN5EvxxqNQDx3kUpKCcPfE',funds=5) 
                    
    addWalletIfNoE(User.objects.get(username='Guillotine'),Currency.objects.get(shortname='XMR'),
                    address='4ABfu85C8qoPGYNrK5pzqc53RJduNoppgFGGo5RTUqGyD6E96yk5v3u7jHkCyh5hox1uokmkKKcMfagnEeowX97BRwSVKXg',funds=200)                
    addWalletIfNoE(User.objects.get(username='Johnny'),Currency.objects.get(shortname='XMR'),
                    address='4ABfu85C8qoPGYNrK5pzqc53RJduNoppgFGGo5RTUqGyD6E96yk5v3u7jHkCyh5hox1uokmkKKcMfagnEeowX97BRwSVKX0',funds=0.5)      
    addWalletIfNoE(User.objects.get(username='Emily'),Currency.objects.get(shortname='XMR'),
                    address='4ABfu85C8qoPGYNrK5pzqc53RJduNoppgFGGo5RTUqGyD6E96yk5v3u7jHkCyh5hox1uokmkKKcMfagnEeowX97BRwSVKX1',funds=0.15)      
    addWalletIfNoE(User.objects.get(username='Stefan'),Currency.objects.get(shortname='XMR'),
                    address='4ABfu85C8qoPGYNrK5pzqc53RJduNoppgFGGo5RTUqGyD6E96yk5v3u7jHkCyh5hox1uokmkKKcMfagnEeowX97BRwSVKX2',funds=100.1)      
    addWalletIfNoE(User.objects.get(username='Heniu'),Currency.objects.get(shortname='XMR'),
                    address='4ABfu85C8qoPGYNrK5pzqc53RJduNoppgFGGo5RTUqGyD6E96yk5v3u7jHkCyh5hox1uokmkKKcMfagnEeowX97BRwSVKX3',funds=44) 
    
    
    addOfferIfNoE(User.objects.get(username='Guillotine'),Currency.objects.get(shortname='PLN'), 
                    type=Offer.Type.SELL, ratetobtc=0.00003445, quantity=3440.2, status=Offer.Status.OPEN)
    addOfferIfNoE(User.objects.get(username='Emily'),Currency.objects.get(shortname='PLN'), 
                    type=Offer.Type.SELL, ratetobtc=0.00003444, quantity=60.11, status=Offer.Status.OPEN)
    addOfferIfNoE(User.objects.get(username='Johnny'),Currency.objects.get(shortname='PLN'), 
                    type=Offer.Type.SELL, ratetobtc=0.00003443, quantity=110.5, status=Offer.Status.OPEN)
    addOfferIfNoE(User.objects.get(username='Stefan'),Currency.objects.get(shortname='PLN'), 
                    type=Offer.Type.BUY, ratetobtc=0.00003441, quantity=10.003, status=Offer.Status.OPEN)
    addOfferIfNoE(User.objects.get(username='Heniu'),Currency.objects.get(shortname='PLN'), 
                    type=Offer.Type.BUY, ratetobtc=0.00003440, quantity=500, status=Offer.Status.OPEN)
    addOfferIfNoE(User.objects.get(username='Vladimir'),Currency.objects.get(shortname='PLN'), 
                    type=Offer.Type.BUY, ratetobtc=0.00003435, quantity=4000, status=Offer.Status.OPEN)
                    
    addOfferIfNoE(User.objects.get(username='Guillotine'),Currency.objects.get(shortname='ZEC'), 
                    type=Offer.Type.SELL, ratetobtc=0.00395000, quantity=0.5, status=Offer.Status.OPEN)
    addOfferIfNoE(User.objects.get(username='Emily'),Currency.objects.get(shortname='ZEC'), 
                    type=Offer.Type.SELL, ratetobtc=0.00398000, quantity=24.2, status=Offer.Status.OPEN)
    addOfferIfNoE(User.objects.get(username='Johnny'),Currency.objects.get(shortname='ZEC'), 
                    type=Offer.Type.SELL, ratetobtc=0.00399000, quantity=50, status=Offer.Status.OPEN)
    addOfferIfNoE(User.objects.get(username='Stefan'),Currency.objects.get(shortname='ZEC'), 
                    type=Offer.Type.BUY, ratetobtc=0.00394000, quantity=0.004, status=Offer.Status.OPEN)
    addOfferIfNoE(User.objects.get(username='Heniu'),Currency.objects.get(shortname='ZEC'), 
                    type=Offer.Type.BUY, ratetobtc=0.00394500, quantity=0.00005, status=Offer.Status.OPEN)
    addOfferIfNoE(User.objects.get(username='Vladimir'),Currency.objects.get(shortname='ZEC'), 
                    type=Offer.Type.BUY, ratetobtc=0.00393500, quantity=0.5, status=Offer.Status.OPEN)
    
    print(User.objects.all())
    print(Currency.objects.all())
    print(Wallet.objects.all())
    print(Offer.objects.all())