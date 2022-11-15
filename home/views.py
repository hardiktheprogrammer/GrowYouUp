from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact, Portfolio, Team, Testimonial

def index(request):
    portfolio = Portfolio.objects.all().order_by('-time')[0:6]
    testimonial = Testimonial.objects.all().order_by('-published_at')[0:3]
    team = Team.objects.all()
    if request.method == 'POST':
        name =request.POST.get('name')
        company_name = request.POST.get('company_name')
        email =request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if len(phone) > 15:
            messages.success(request,'Phone no. too long,please check again')
            return HttpResponseRedirect(reverse('index:index'))
        elif len(company_name) > 50:
            messages.success(request,'Company Name too big')
            return HttpResponseRedirect(reverse('index:index'))
        entry = Contact(name=name,company_name=company_name,email=email,phone=phone,message=message)
        entry.save()
        data={
            'name':name,
            'company_name':company_name,
            'email':email,
            'phone':phone,
            'message':message
        }
        message='''
        New Order : {}
        from : {}
        '''.format(data['message'],data['email'])
        send_mail(data['company_name'],message,'',['growyouup007@gmail.com'],fail_silently=False)
        messages.success(request,'Thanks for contacting,our team will connect with you soon!')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request,'index/index.html',{'portfolio':portfolio,'testimonial':testimonial,'team':team})