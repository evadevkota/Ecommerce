from django.contrib import admin
from .models import AddToCart,ProductBuyerInfo



class AddToCartCustomize(admin.ModelAdmin):
    list_display = ['user','cart_title', 'cart_price', 'cart_type', 'cart_category']


class ProductBuyerInfoCustomize(admin.ModelAdmin):
    list_display = ['user','total_price', 'date']


admin.site.register(AddToCart,AddToCartCustomize)


admin.site.register(ProductBuyerInfo,ProductBuyerInfoCustomize)
