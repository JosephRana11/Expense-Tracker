from django.db import models
from users.models import CustomUser

currency_choice = (
    ('USD' , 'USD'),
    ('NPR' , 'NPR'),
    ('INR' , 'INR'),
    ('YEN' , 'YEN'),
)

class Wallet(models.Model):
    wallet_owner = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    wallet_name = models.CharField(max_length=70)
    wallet_currency = models.CharField(max_length=20 , choices=currency_choice)
    wallet_capital = models.DecimalField(max_digits=12, decimal_places=2)
    wallet_creation_date = models.DateField(auto_now_add=False , auto_now=True)
    wallet_edited_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.wallet_owner}-{self.wallet_name}'
    
