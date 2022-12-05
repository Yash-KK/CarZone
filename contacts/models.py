from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car_id = models.IntegerField()
    car_price = models.IntegerField()
    user_id = models.IntegerField()
    customer_need = models.CharField(max_length=255)
    car_title = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10, blank=True)
    message = models.TextField(blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"For {self.car_title}"
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contact's"
        
    
    