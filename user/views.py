from django.shortcuts import render,HttpResponseRedirect
from .forms import  Frm , Post
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
#from products.models import Product
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(requset):
    if requset.method == 'POST':
        fm = Frm(requset.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/user_login/')    
    else:
        fm = Frm()
    return render(requset, 'signup.html',{'form':fm}) 

def post(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
                fm = Post(request.POST)
                if fm.is_valid():
                    fm.save()
        else:
                fm = Post()
        return render(request,'post.html',{'form':fm})  
    else:
        return HttpResponseRedirect('/user_login/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'logged in successfully !!')
                    return HttpResponseRedirect('/post/')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/post/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')