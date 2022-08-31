from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from ratelimit.decorators import ratelimit
from .models import Contact, Portfolio, Team, Testimonial


@ratelimit(key='ip',rate='5/d',method=['POST'])
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
        entry = Contact(name=name,company_name=company_name,email=email,phone=phone,message=message)
        entry.save()
        messages.success(request,'Thanks will get back to u ASAP!')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request,'index/index.html',{'portfolio':portfolio,'testimonial':testimonial,'team':team})