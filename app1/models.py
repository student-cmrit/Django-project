from django.db import models

# Create your models here.
# models.py

from django.db import models

class Employee(models.Model):
    # Fields for employee details
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    designation = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    # Image upload field
    profile_image = models.ImageField(upload_to='employee_images/', null=True, blank=True)

    def __str__(self):
        return self.name
