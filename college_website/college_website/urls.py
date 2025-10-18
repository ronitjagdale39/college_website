# CORRECTED main urls.py file

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # For any URL that isn't 'admin/', look in the 'web.urls' file.
    path('', include('web.urls')), 
]