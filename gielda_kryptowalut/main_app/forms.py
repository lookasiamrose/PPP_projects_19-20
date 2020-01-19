from django import forms
from .models import Offer
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class OfferForm(forms.ModelForm):
	class Meta:
		model = Offer
		fields = [ 'currencyid', 'type', 'ratetobtc', 'quantity']
		labels = {
            'currencyid': _('Currency'),
            'type': _('Buy/Sell'),
            'ratetobtc': _('Rate'),
            'quantity': _('Quantity'),
        }