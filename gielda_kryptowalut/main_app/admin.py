from django.contrib import admin
from .models import Currency
from .models import Offer
#from .models import User
from .models import Wallet

admin.site.register(Currency)
admin.site.register(Offer)
#admin.site.register(User)
admin.site.register(Wallet)
