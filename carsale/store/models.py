from django.db import models

# Create your models here.
class Sold_Cars(models.Model):
    brand=models.CharField(max_length=50)
    equipment = models.TextField(max_length=300)
    picture = models.ImageField(upload_to='car_images/', blank=True)

def __str__(self):
    return self.brand
