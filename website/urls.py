from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name='home'),
    path('about', AboutPage, name='about'),
    path('login', LoginPage, name='login'),
    path('register', RegisterPage, name='register'),
    path('logout', LogoutPage, name='logout'),
    path('doctor/<int:pk>', DcotorPage, name='doctor'),
    path('doctor/queue/<int:pk>', DcotorQueuePage, name='queue'),
]