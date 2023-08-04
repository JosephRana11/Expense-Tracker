from django import forms 
from .models import Wallet 

class WalletForm(forms.ModelForm): 
    class Meta:
     model = Wallet
     fields = ['wallet_name' , 'wallet_currency' , 'wallet_capital']