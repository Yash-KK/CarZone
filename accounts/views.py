#DJANGO
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#MODELS
from contacts.models import (
    Contact
)
# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        messages.info(request, "Already a logged In User")
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
                
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully Logged-in')
            return redirect('dashboard')      
        else:
            messages.error(request, "Invalid Credentials")
                   
    return render(request, 'accounts/login.html')

def register_page(request):
    if request.user.is_authenticated:
        messages.info(request, "Already a logged In User")
        return redirect('dashboard')
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        username = request.POST['username']
        email = request.POST['email']
        
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        print(first_name, last_name, username, email, password, confirm_password)
        
        if password != confirm_password:
            messages.error(request, "Password's do not Match!")
            return redirect('register-page')
        # create user instance        
        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username        
        user.set_password(password)
        user.save()
        
        messages.success(request, 'User registered Successfully!')
        return redirect('login-page')
    
    return render(request, 'accounts/register.html')

@login_required(login_url='login-page')
def dashboard(request):
    inquiries = Contact.objects.filter(user_id=request.user.id)    
    context = {
        'inquiries': inquiries
    }
    return render(request, 'accounts/dashboard.html', context)

def logout_function(request):    
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('login-page')