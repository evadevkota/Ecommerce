from django.urls import path
from .views import create_cart,open_cart,delete_cart_method,total_Price,checkout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("open_Cart",open_cart,name="open_cart"),
    path("create-my-cart",create_cart,name="create_my_cart"),
    path("delete-my-cart/<int:id>",delete_cart_method,name="delete_cart"),
    path("total-price",total_Price,name="total_price"),
    path("checkout",checkout, name="checkout")
    
  
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)