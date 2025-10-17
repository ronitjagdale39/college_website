from django.urls import path
from . import views

urlpatterns = [
    # This will be the root URL of your app (e.g., /resource_hub/)
    path('', views.resource_hub, name='resource_hub'),
    
    # This will be a specific URL for the about page (e.g., /resource_hub/about/)
    path('about.html', views.about, name='about'),
    path('signup.html',views.signup_view,name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
   
