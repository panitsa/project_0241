#models.py
from django.db import models
from django.contrib.auth.models import *
from django import forms

class Representative(models.Model):
    image = models.ImageField(upload_to='Representative_images/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    
class Activity_news(models.Model):
    image = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/', null=True)
    text = models.TextField()
    time = models.TimeField()
    date = models.DateField()
    
class Villagepublic(models.Model):
    image = models.ImageField(upload_to='Villagepublic_images/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

class Income_expenses(models.Model):
    date = models.DateField()
    time = models.TimeField()
    income = models.TextField()
    expenses = models.TextField()
    image = models.ImageField(upload_to='Income_expenses_images/')

class Useregister(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=15)

class Userlogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    
    