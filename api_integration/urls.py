# api_integration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api-data/', views.api_data_view, name='api_data'),
]
