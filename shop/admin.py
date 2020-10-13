from django.contrib import admin
# class Products is in models.py is imported to register the Product table in website under admin page
from .models import Products
# Register your models here.

admin.site.register(Products)
