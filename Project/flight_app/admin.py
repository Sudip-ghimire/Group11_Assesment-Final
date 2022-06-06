from django.contrib import admin
from flight_app.models import Book, Destiny, Passenger

myModels= [Book,Destiny,Passenger]
admin.site.register(myModels)
# Register your models here.

