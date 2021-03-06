"""djangoapi_rest_object URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    url(r'car/$', views.car, name='car'),
    url(r'car/(?P<id_car>\d+)$', views.car, name='carid'),
    url(r'car/(?P<cursor>\d+)/(?P<amount>\d+)$', views.car, name='caramount'),
    url(r'carwithauth/$', views.carwithauth, name='car'),

    url(r'caruser/$', views.caruser, name='car'),
    url(r'caruser/(?P<id_car>\d+)$', views.caruser, name='carid'),
    url(r'caruser/(?P<cursor>\d+)/(?P<amount>\d+)$', views.caruser, name='caramount'),
]
