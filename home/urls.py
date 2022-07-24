from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('team/',views.team,name='team'),
    path('contact/',views.contact,name='contact'),
    path('portfolio/',views.portfolio,name='portfolio')

]