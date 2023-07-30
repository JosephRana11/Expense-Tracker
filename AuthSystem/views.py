from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from users.models import CustomUser
from users.forms import CustomUserCreationForm
from django.urls import reverse

@login_required(login_url='login')
def home_view(request):
    return render(request , 'home.html')

def login_view(request):
    if request.method == 'POST':
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        user = authenticate(email = uemail , password = upassword)
        if user is not None:
            login(request , user)
            return redirect(reverse('home'))
        else:
            error_msg = "Invalid email or password.Please Try again"
            return render(request , 'login.html' , {'error_msg':error_msg})
    else: 
     return render(request , 'login.html')

def register_view(request):
    if request.method == 'POST':
        uemail = request.POST.get('email')
        upass1 = request.POST.get('password1')
        upass2 = request.POST.get('password2')
        form = CustomUserCreationForm(data = {'email' : uemail , 'password1' : upass1 ,'password2' : upass2 })
        if form.is_valid():
            form.save()
            return redirect(reverse('create-wallet'))
        else:
            return render(request , 'registration.html')
    else:
     return render(request , 'registration.html')

def test_view(request):
    return render(request , 'test.html' , {'form':CustomUserCreationForm})

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))