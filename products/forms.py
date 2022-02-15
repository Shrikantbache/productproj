from django.core import validators
from django.db.models import fields
from django import forms
from .models import Productss 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class Product(forms.ModelForm):
    class Meta:
        model = Productss
        fields = ['name','weight','price']
        app_label = 'products'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'weight': forms.EmailInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            
        }














