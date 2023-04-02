from django.shortcuts import render
from .models import Banner,Category,Brand,Product,ProductAttribute

# Create your views here.

def home(request):
    return render(request,'index.html')


# def home(request):
# 	banners=Banner.objects.all().order_by('-id')
# 	data=Product.objects.filter(is_featured=True).order_by('-id')
# 	return render(request,'index.html',{'data':data,'banners':banners})