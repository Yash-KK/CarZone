#Django
from django.shortcuts import render
from django.db.models import Q

#MODELS
from pages.models import (
    Team
)
from cars.models import (
    Car
)

# Create your views here
def home(request):
    team = Team.objects.order_by('-created_at')
    featured_cars = Car.objects.filter(is_featured=True)
    all_cars = Car.objects.all().order_by('-created_date')
    
    model_fields = Car.objects.values_list('model', flat=True).distinct() 
    year_fields = Car.objects.values_list('year', flat=True).distinct()
    state_fields = Car.objects.values_list('state', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()
    color_fields = Car.objects.values_list('color', flat=True).distinct()
    
    context = {
        'team' : team,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        
        'model_field': model_fields,
        'year_field': year_fields,
        'state_field': state_fields,
        'body_style_field': body_style_fields,
        'color_field': color_fields,
        
        
    }
    
    return render(request, 'home.html', context)

def search(request):
    cars = Car.objects.all().order_by('-created_date')
    
    model_fields = Car.objects.values_list('model', flat=True).distinct() 
    year_fields = Car.objects.values_list('year', flat=True).distinct()
    state_fields = Car.objects.values_list('state', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()
    color_fields = Car.objects.values_list('color', flat=True).distinct()
    transmission_fields = Car.objects.values_list('transmission', flat=True).distinct()
    
    try:
        if 'search' not in request. META['HTTP_REFERER']:
            if request.method == 'GET':
                key = request.GET['keyword']
                if key:            
                    cars = Car.objects.filter(description__icontains = key)
    except:
        pass
    
    if 'model' in request.GET:
        key = request.GET['model']
        if key:
            cars = Car.objects.filter(model=key)

    if 'color' in request.GET:
        key = request.GET['color']
        if key:
            cars = Car.objects.filter(color=key)

    if 'year' in request.GET:
        key = request.GET['year']
        if key:
            cars = Car.objects.filter(year=key)

    if 'state' in request.GET:
        key = request.GET['state']
        if key:
            cars = Car.objects.filter(state=key)

    if 'body_style' in request.GET:
        key = request.GET['body_style']
        if key:
            cars = Car.objects.filter(body_style=key)
    
    if 'transmission' in request.GET:
        key = request.GET['transmission']
        if key:
            cars = Car.objects.filter(transmission=key)
    
    context = {
        'cars': cars,
        
        'model_field': model_fields,
        'year_field': year_fields,
        'state_field': state_fields,
        'body_style_field': body_style_fields,
        'color_field': color_fields,
        'transmission_field': transmission_fields
        
    }            
    return render(request, 'search.html', context)

