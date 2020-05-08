from django.contrib import admin
from django.urls import path,include
from . import views


app_name= 'my_docs'
urlpatterns = [
    path('', views.index, name='list_of_items'),
    
]
