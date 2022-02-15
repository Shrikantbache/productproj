from ast import Pass
from django.contrib import admin
from .models import Productss
# Register your models here.
class Productadmin(admin.ModelAdmin):
    list_display = ('name','weight','price','created_at','updated_at')

admin.site.register(Productss,Productadmin)

