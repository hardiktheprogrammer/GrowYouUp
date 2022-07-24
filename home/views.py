from django.shortcuts import render

def index(request):
    return render(request,'index/index.html')

def about(request):
    return render(request,'index/about.html')

def services(request):
    return render(request,'index/services.html')

def team(request):
    return render(request,'index/team.html')

def contact(request):
    return render(request,'index/contact.html')

def portfolio(request):
    return render(request,'index/portfolio.html')