from rest_framework import  generics
from django.shortcuts import render

# Create your views here.
from .serializers import MenuSerializer
from .serializers import BannerSerializer
from .serializers import AboutSerializer
from .serializers import PartnerSerializer
from .serializers import ComicSerializer
from .serializers import DrinkSerializer
from .serializers import FoodSerializer
from .serializers import BannerPkSerializer

from .models import Menu
from .models import Banner
from .models import Partner
from .models import Comic
from .models import About
from .models import Drink
from .models import Product
from .models import Food
from .serializers import ProductSerializer

class BannerPkDetailAPIView(generics.RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerPkSerializer
    lookup_field = 'pk'


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MenuAPIView(generics.ListAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer


class BannerAPIView(generics.ListAPIView):
    queryset=Banner.objects.all()
    serializer_class=BannerSerializer


class AboutAPIView(generics.ListAPIView):
    queryset=About.objects.all()
    serializer_class=AboutSerializer


class PartnerAPIView(generics.ListAPIView):
    queryset=Partner.objects.all()
    serializer_class=PartnerSerializer

class FoodAPIView(generics.ListAPIView):
    queryset=Food.objects.all()
    serializer_class=FoodSerializer

class ComicAPIView(generics.ListAPIView):
    queryset=Comic.objects.all()
    serializer_class=ComicSerializer




class DrinkAPIView(generics.ListAPIView):
    queryset=Drink.objects.all()
    serializer_class=DrinkSerializer
