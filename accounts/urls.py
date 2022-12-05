from django.urls import path

#VIEWS
from .import views
urlpatterns = [
    path('login/', views.login_page, name='login-page'),
    path('register/', views.register_page, name='register-page'),
    path('logout-function/', views.logout_function, name='logout-function'),
    
    path('dashboard/', views.dashboard, name='dashboard')
    
    
]
