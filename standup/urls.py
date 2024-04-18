# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('stand_up_admin.urls')),
     path('api_main/', include('api_integration.urls')),
]
