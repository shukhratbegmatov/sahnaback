from rest_framework import serializers
from .models import Menu
from .models import Banner
from .models import Comic
from .models import Partner
from .models import About
from .models import Drink
from .models import Food

from .models import Product

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields = ['id','title','link']

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id','name','description','type','price','url','date_time','images','status']

class BannerPkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields =  ['id','name','description','type','price','url','date_time','images','status']


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = ['first_name','last_name','bio','telegram','instagram','images']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['name','url','images']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields =['name','description','price']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields =  ['title','description','address','work_time','phone','messenger_url']




class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['title','description','price']



