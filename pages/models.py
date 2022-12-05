from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='Images/Profile Pic')
    
    facebook_link = models.URLField(max_length=255) 
    twitter_link = models.URLField(max_length=255)
    gmail_link = models.URLField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = "Team's"

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    