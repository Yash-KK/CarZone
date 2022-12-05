#DJANGO
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#MODELS
from .models import (
    Car
)
# Create your views here.
def cars(request):
    all_cars = Car.objects.all().order_by('-created_date')
    
    
    model_fields = Car.objects.values_list('model', flat=True).distinct() 
    year_fields = Car.objects.values_list('year', flat=True).distinct()
    state_fields = Car.objects.values_list('state', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()
    color_fields = Car.objects.values_list('color', flat=True).distinct()
    
    #paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(all_cars, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
        
    context = {
        'all_cars': users,
        
        
        'model_field': model_fields,
        'year_field': year_fields,
        'state_field': state_fields,
        'body_style_field': body_style_fields,
        'color_field': color_fields,
  
    }
    return render(request, 'cars/cars.html', context)

def car_detail(request, id):    
    car = Car.objects.get(id=id)    
    context = {
        'car': car
    }    
    return render(request, 'cars/car_detail.html', context)

