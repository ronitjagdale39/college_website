from django.urls import path
from . import views

urlpatterns = [
   
    
    path('', views.resource_hub, name='resource_hub'),

]