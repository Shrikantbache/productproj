from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import Product 
from .models import Productss
#from products.models import Product
# Create your views here.

def productinfo(request):
    if request.method == 'POST':
            fm = Product(request.POST)
            if fm.is_valid():
                fm.save()
    else:
            fm = Product()
    return render(request,'products.html',{'form':fm})  




def productinfo(request):
    if request.method == 'POST':
        fm = Product(request.POST)
        if fm.is_valid():
            
            fm.save()
            fm = Product()
    else:
        fm = Product()
    prod = Productss.objects.all()
    return render(request,'product.html',{'form':fm,'pro':prod})


def update(request,id):
    if request.method == 'POST':
         pi = Productss.objects.get(pk = id)
         fm = Product(request.POST,instance=pi)  
         if fm.is_valid():
            fm.save()
    else:
        pi = Productss.objects.get(pk = id)
        fm = Product(instance=pi)
        return render(request,'update.html',{'form':fm})
    return render(request,'update.html',{'form':fm})

def delete_data(request,id):
    if request.method == 'POST':
        pi = Productss.objects.get(pk = id) 
        pi.delete()
        return HttpResponseRedirect('/')
