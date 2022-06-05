from unicodedata import name
from django.db import models
from django import forms
from .widget import DatePickerInput
from flight_app import widget

# Create your models here.

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=50,null=True)
    PassportNumber= models.CharField(max_length=60,null=True)
    DepartureDate= models.CharField(max_length=60,null=True)
    ReturnDate = models.CharField(max_length=60,null=True)
    destination = models.CharField(max_length=60,null=True)
    
    def __str__(self):
        return self.name




class Destiny(models.Model):
    d_name = models.CharField(max_length=30)
    d_destination = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s' % (self.name, self.destination)

class Passenger(models.Model):
    p_name = models.CharField(max_length=100)
    Destiny= models.ManyToManyField(Destiny)
    p_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    p_returndate = models.DateField()

    def __str__(self):
        return str(self.id) + " : " + self.title
