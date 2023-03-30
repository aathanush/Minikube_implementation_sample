from django.shortcuts import render, redirect
from django.http import JsonResponse
import pickle
import joblib
import PIL
import os
import pickle
from mpl_toolkits.axes_grid1 import ImageGrid
import math
from product.models import Product
def shop_site(request):
    data = Product.objects.all()
    print(data[0].desc)
    print(data)
    return render(request,'index.html',{'product':data})
