from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Offer(models.Model):
    userid = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='offers',
    )
    currencyid = models.ForeignKey(
        'Currency',
        on_delete=models.CASCADE,
        related_name='offers',
    )
    
    class Type(models.TextChoices):
        SELL = 'SELL', _('Sell')
        BUY = 'BUY', _('Buy')
        UNDEFINED = 'Undefined', _('N/A')
    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.UNDEFINED,
    )
    
    ratetobtc = models.DecimalField(max_digits=12,decimal_places=8)
    quantity = models.DecimalField(max_digits=20,decimal_places=8)
    
    class Status(models.TextChoices):
        OPEN = 'OPEN', _('Open')
        CLOSED = 'CLOSED', _('Closed')
        UNDEFINED = 'Undefined', _('N/A')
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.UNDEFINED,
    )
    time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.type + ' ' + str(self.ratetobtc) + ' ' + str(self.quantity) + ' ' + self.status
    
#class User(models.Model):
    #username = models.CharField(max_length=255)
    #email = models.EmailField()
    #password = models.CharField(max_length=255)
    
    #def __str__(self):
        #return self.username + ' ' + self.email

class Currency(models.Model):
    shortname = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    logopath = models.CharField(max_length=255) 
    
    def __str__(self):
        return self.shortname + ' ' + self.name + ' ' + self.logopath

class Wallet(models.Model):
    userid = models.ForeignKey(
        User,
        on_delete=models.SET(1),
        related_name='wallets',
    )
    currencyid = models.ForeignKey(
        'Currency',
        on_delete=models.SET(1),
        related_name='wallets',
    )
    address = models.CharField(max_length=255)
    funds = models.DecimalField(max_digits=20,decimal_places=8) 
    
    def __str__(self):
        return self.address + ' ' + str(self.funds)