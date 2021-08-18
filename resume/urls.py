from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send-gmail/', views.send_gmail, name='send-mail')
]