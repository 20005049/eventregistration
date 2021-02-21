from django.db import models

# Create your models here.
from django.contrib import admin
class participatents(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    
    
class participatentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email','phone') 

