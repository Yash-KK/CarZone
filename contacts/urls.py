from django.urls import path

#VIEWS
from .import views

urlpatterns = [
    path('inquiry/', views.inquiry, name='inquiry')
]
