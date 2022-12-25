from django.contrib import admin
from django.urls import path
from aero import views

urlpatterns = [
    path("", views.index, name="Aero.Viz")
    # path("index.html", views.index, name="Aero.Viz")
    
 
   
]
