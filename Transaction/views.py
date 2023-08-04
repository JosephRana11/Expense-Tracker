from django.shortcuts import render , reverse , redirect
from .forms import Income_Form
from Capital import Wallet

def record_income_view(request):
    if request.method == 'POST':
        request_income_amount = request.POST.get('Income_Amount')
        request_income_type = request.POST.get('Income_Type')
        request_income_note = request.POST.get('Income_Note')
        print(request_income_amount , request_income_type , request_income_note)
        form_data = {
            'amount' : request_income_amount , 
            'income_type' : request_income_type,
            'income_note' : request_income_note
        }
        form = Income_Form(data=form_data)
        if form.is_valid():
            record = form.save(commit = False)
            record.parrent_wallet = request.user
            record.save()
        else:
            print("Form Invalid")
        return redirect(reverse('home'))
        
    else:
     wallets = 
     return render(request , 'record-income.html' , {'form':Income_Form})