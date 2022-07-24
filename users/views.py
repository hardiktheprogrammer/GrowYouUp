from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'users/signup.html')
            elif len(password) <8:
                messages.info(request,'ATLEAST 8 CHARACTER PASSWORD NEEDED')
                return render(request,'users/signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'users/signup.html')
            else:
                entry=User.objects.create_user(username=username,email=email,password=password)
                entry.save()
                messages.success(request,'Account Registered Succesfully!')
                return HttpResponseRedirect(reverse('users:login'))
        else:
            messages.info(request,'Password and confirm password didn"t match')
    return render(request,'users/signup.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'Logout Successful')
    return HttpResponseRedirect(reverse('index:index'))