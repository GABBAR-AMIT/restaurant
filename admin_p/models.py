from django.db import models

# Create your models here.

class UserDetails(models.Model):
    name=models.CharField( max_length=50)
    mobile=models.CharField(max_length=15, unique=True)
    email=models.CharField(max_length=50)
    
