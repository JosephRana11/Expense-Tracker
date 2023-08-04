from django.shortcuts import render , HttpResponse , redirect
from .models import Wallet
from .forms import WalletForm
from django.urls import reverse

def create_wallet_view(request):
    if request.method == 'POST':
        for key , value in request.POST.items():
            print(f"{key}:{value}")
        print(request.user)
        wallet_creation_name = request.POST.get('WalletName')
        wallet_creation_capital = request.POST.get('WalletCapital')
        wallet_creation_currency = request.POST.get('WalletCurrency')
        form_data = {
            'wallet_name' : wallet_creation_name,
            'wallet_currency' : wallet_creation_currency , 
            'wallet_capital' : wallet_creation_capital,
        }
        form = WalletForm(data=form_data)
        if form.is_valid():
            firstwallet = form.save(commit=False)
            firstwallet.wallet_owner = request.user
            firstwallet.save()
            return redirect(reverse('all-wallet'))
            
        else:
            return HttpResponse("You tried entering wrong details.")

        return HttpResponse("Working")
    return render(request , 'create-wallet.html' , {'form':WalletForm})


def all_wallet_view(request):
    obj = Wallet.objects.filter(wallet_owner=request.user)
    return render(request , 'all-wallet.html', {'obj':obj})

def edit_wallet_view(request , walletid):
    item = Wallet.objects.get(pk = walletid)
    if request.method == 'POST':
        wallet_creation_name = request.POST.get('WalletName')
        wallet_creation_capital = request.POST.get('WalletCapital')
        item.wallet_name = wallet_creation_name
        item.wallet_capital = wallet_creation_capital
        item.save()
        return redirect(reverse('all-wallet'))
    
    else:
     return render(request , 'edit-wallet.html', {'item':item})

