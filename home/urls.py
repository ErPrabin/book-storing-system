from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index,name='index'),
    path('booking', views.booking,name='booking'),
]