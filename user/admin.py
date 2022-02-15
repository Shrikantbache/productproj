from ast import Pass
from django.contrib import admin
from .models import Post
# Register your models here.

class Postadmin(admin.ModelAdmin):
    
    list_display = ('user','text','created_at','updated_at')

admin.site.register(Post,Postadmin)