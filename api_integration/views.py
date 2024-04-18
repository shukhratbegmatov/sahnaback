# api_integration/views.py
from django.shortcuts import render
from .api import get_api_data

def api_data_view(request):
    api_data = get_api_data()
    return render(request, 'api_integration/api_data.html', {'api_data': api_data})

