from django.contrib import admin
from django.urls import path
from .views import home,product_details 

urlpatterns = [
    path('',home, name='home'),
    path('product/details',product_details, name='product_details'),
]