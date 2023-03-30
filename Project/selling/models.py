from django.db import models
from django import forms
# Create your models here.
class Retailer(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.TextField(max_length=100)
    verified = models.BooleanField(default=False)
    certificate = models.ImageField(default='./shopping/no_image.jpg',upload_to='')

class LoginForm(forms.Form):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.TextField(max_length=100)
    certificate = models.ImageField(default='./shopping/no_image.jpg',upload_to='')
