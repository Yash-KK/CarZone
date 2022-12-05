#DJANGO
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from CarZone.settings import EMAIL_HOST_USER
#MODELS
from .models import (
    Contact
)
# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        car_price = request.POST['car_price']
        car_id = request.POST['car_id']
        
        city = request.POST['city']
        state = request.POST['state']
        
        email = request.POST['email']
        phone = request.POST['phone']
        
        message = request.POST['message']
        
        print(user_id, first_name, last_name, customer_need, car_title, car_price, car_id, city, state, email, phone, message)
        contact = Contact()
        contact.first_name = first_name
        contact.last_name = last_name
        contact.car_id = car_id
        contact.car_price = car_price
        contact.user_id = user_id
        contact.customer_need = customer_need
        contact.car_title = car_title
        contact.city = city
        contact.state = state
        contact.email = email
        contact.phone_number = phone
        contact.message = message
        
        if_exists = Contact.objects.filter(user_id=user_id, car_id=car_id).exists()
        if if_exists:
            messages.error(request, 'You have already sent an inquiry for this Car')
            return redirect('/cars/cars/'+ car_id)
                
        contact.save()
        
        # send email
        subject = f"Inquiry received for a {car_title}"
        message = f"You have a new inquiry for the Car {car_title} from {email}. Please login to admin Panel"
        email_from = 'admin@gmail.com'
        recipient_list = [EMAIL_HOST_USER]
        send_mail(subject, message, email_from, recipient_list)
        
        
        messages.success(request, 'Message Sent. Will get in touch in few days')
        return redirect('/cars/cars/' + car_id)


