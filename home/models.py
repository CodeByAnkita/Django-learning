from django.db import models

# Create your models here.

class Student(models.Model):
    # Fields for the Student model
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True )
    address = models.TextField(null=True, blank=True )
    # image = models.ImageField()  # Optional: specify the upload directory
    # file = models.FileField()  # Optional: specify the upload directory



class car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

def __str__(self)-> str:
    return self.car_name