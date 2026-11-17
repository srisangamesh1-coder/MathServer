from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [path('', views.calculate_rate, name='calculate_rate'),]