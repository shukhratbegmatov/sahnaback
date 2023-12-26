"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import MenuAPIView
from .views import BannerAPIView
from .views import AboutAPIView
from .views import PartnerAPIView
from .views import ComicAPIView
from .views import DrinkAPIView
from .views import FoodAPIView
from .views import ProductListAPIView
from .views import BannerPkDetailAPIView

urlpatterns = [
    path('menu', MenuAPIView.as_view()),
    path('banners', BannerAPIView.as_view()),
    path('about', AboutAPIView.as_view()),
    path('partner', PartnerAPIView.as_view()),
    path('comic', ComicAPIView.as_view()),
    path('food_menu', FoodAPIView.as_view()),
    path('drink', DrinkAPIView.as_view()),
    path('food_menudsadsad', ProductListAPIView.as_view()),
      path('pk_id/<int:pk>/', BannerPkDetailAPIView.as_view(), name='product-detail'),
]
