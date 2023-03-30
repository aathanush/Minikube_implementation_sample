from django.shortcuts import render, redirect
from django.http import JsonResponse
import pickle
import joblib
import PIL
import os
import pickle
from mpl_toolkits.axes_grid1 import ImageGrid
import math
from selling.models import Retailer, LoginForm
from django.core.mail import send_mail
def register(request):
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         
         username = MyLoginForm.cleaned_data['username']
         password = MyLoginForm.cleaned_data['password']
         certificate = MyLoginForm.cleaned_data['certificate']
         email= MyLoginForm.cleaned_data['email']

         send_mail('Shopping portal retailer verification', 'Your data has been received by us successfully. Please wait for 2-3 days to get verified as a retailer on our portal. Thank you for your understanding!','thanush@student.tce.edu', recipient_list, fail_silently=False, auth_password='Password=TCE20H055')
         return render(request,'manufacturer.html',{'message':'Check your Mail!'})
   else:
      MyLoginForm = LoginForm()
      return render(request,'manufacturer.html',{'message':'Registration Unsuccessful. Please try again!'})
    
