from django.urls import path

# Views
from .import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact')
]
