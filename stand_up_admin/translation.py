from modeltranslation.translator import register, TranslationOptions

from .models import Menu
from .models import Banner
from .models import About
from .models import Comic
from .models import Drink
from .models import Product
from .models import Food

@register(Food)
class FoodTranslationOptions(TranslationOptions):
    fields = ('name','description')

@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Banner)
class TopBannerTranslationOptions(TranslationOptions):
        fields = ('name','description','type')

@register(About)
class AboutTranslationOptions(TranslationOptions):
        fields = ('title','description','address')

@register(Comic)
class ComicTranslationOptions(TranslationOptions):
        fields = ('first_name','last_name','bio')






@register(Product)
class ProductTranslationOptions(TranslationOptions):
        fields = ('name','description')


@register(Drink)
class DrinkTranslationOptions(TranslationOptions):
        fields = ('title','description')