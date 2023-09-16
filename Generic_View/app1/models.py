from django.db import models
from django.urls import reverse

# Create your models here.

class Movies(models.Model):
    
    name=models.CharField(max_length=50)
    date=models.DateField()
    
    
    def __str__(self):
        
        return f'{self.name}'
    
    
    
    
    
    