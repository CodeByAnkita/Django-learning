from django.db import models

# Create your models here.

class Student(models.Model):
    # Fields for the Student model
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()  # Optional: specify the upload directory
    file = models.FileField()  # Optional: specify the upload directory

    # def __str__(self):
    #     return self.name  # Returns the name when the object is printed

class Product(models.Model):
    # Define fields for the Product model as needed
    pass
