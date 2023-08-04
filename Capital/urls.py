from django.urls import path
from .views import create_wallet_view , all_wallet_view , edit_wallet_view 

urlpatterns = [
    path('create-wallet' , create_wallet_view , name='create-wallet') ,
    path('all-wallets' , all_wallet_view , name='all-wallet'),
    path('edit-wallet/<int:walletid>' , edit_wallet_view , name = 'edit-wallet'),
]
