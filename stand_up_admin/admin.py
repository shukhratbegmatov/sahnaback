from django.contrib import admin

from .models import Menu
from .models import Banner
from .models import Partner
from .models import Comic
from .models import About
from .models import Product

from .models import Food
from .models import Drink
from .models import Drink_Category

admin.site.register(Menu)
admin.site.register(Comic)
admin.site.register(Banner)
admin.site.register(Partner)
admin.site.register(About)
admin.site.register(Food)

admin.site.register(Product)
admin.site.register(Drink)
admin.site.register(Drink_Category)