"""flight_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from flight_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^add/booking/?$', views.add_booking,name='book'),
    re_path(r'^add/booking/done/?$', views.add_booking_submit,name='homepage'),
    re_path(r'^add/booking/15?$', views.edit_booking, name='edit2'),
    re_path(r'^add/booking/(?P<key>\d+)?/?$', views.edit_booking),
    re_path(r'^delete/booking/(?P<key>\d+)?/?$', views.delete_booking),
    re_path(r'^delete/booking/9?$', views.delete_booking,name='del'),
    re_path(r'^ /add/booking/add/booking/done?$', views.add_booking,name='booking'),
    url(r'^$', views.Home, name='Home'),
    url(r'^link_2/?$', views.add_booking, name = 'link_2'),
    url(r'^link_3/?$', views.add_booking, name = 'link_3'),
    url(r'^contact_us/?$', views.contact_us, name = 'contact_us'),
    url(r'^FAQ/?$', views.FAQ, name = 'FAQ'),
   



    ]
