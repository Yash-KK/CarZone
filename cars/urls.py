from django.urls import path

#VIEWS
from .import views
urlpatterns = [
    path('cars/', views.cars, name='cars'),
    path('cars/<int:id>/', views.car_detail, name='car-detail')
]
