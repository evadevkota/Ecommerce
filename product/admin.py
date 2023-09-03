from django.contrib import admin
from .models import Product

class ProductCustomize(admin.ModelAdmin):
    list_display=['title','price','type','image','category']

admin.site.register(Product,ProductCustomize)





