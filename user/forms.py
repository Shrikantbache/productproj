from django.core import validators
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Frm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'})
            
            
        }
        

class Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'text']
        widgets = {
            
            
            'text':forms.Textarea(attrs={'class': 'form-control' })
       }


