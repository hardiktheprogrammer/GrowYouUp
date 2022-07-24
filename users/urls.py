from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',views.logout,name='logout')

]