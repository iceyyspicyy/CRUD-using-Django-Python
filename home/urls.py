from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('home', views.home, name='home' ),
    path('about', views.about, name='about'),
    path('messages', views.messages, name='messages'),
    path('contact', views.contact, name='contact'),
    path('accounts', include('django.contrib.auth.urls')),
]
    