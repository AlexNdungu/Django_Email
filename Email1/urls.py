from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('sendEmail/',send_email,name='send_email'),
]