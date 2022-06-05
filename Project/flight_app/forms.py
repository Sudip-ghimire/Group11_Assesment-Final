
from django import forms
from .models import *
from .widget import DatePickerInput

class Booking (forms.ModelForm):
    class Meta:
        model = Book

        fields = ['name', 'address','PassportNumber','DepartureDate','ReturnDate','destination']

        label = {
           
            'address': 'Postal Address',
           
        }
       

  



    