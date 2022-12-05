from django.shortcuts import render
from django.core.mail import send_mail
from CarZone.settings import EMAIL_HOST_USER
from django.contrib import messages 
#MODELS
from .models import (
    Team
)
# Create your views here.

def about(request):
    team = Team.objects.order_by('-created_at')
    context = {
        'team': team
    }
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']        
        message = request.POST['message']
        
        print(name, email, subject, phone, message)

        # send emeil
        subject = f"{subject}"
        message = f"{message}: \n From: {email}. Phone: {phone}"
        email_from = 'admin@gmail.com'
        recipient_list = [EMAIL_HOST_USER,]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, "Will reach out to you Shortly!")
        
        
    return render(request, 'pages/contact.html')
