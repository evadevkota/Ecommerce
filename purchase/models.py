from django.db import models

from django.contrib.auth.models import User

class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    cart_title = models.CharField(max_length=100,null=True)
    cart_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cart_type = models.CharField(max_length=100,null=True)
    
    cart_category = models.CharField(max_length=100,null=True)

class ProductBuyerInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    date = models.DateField(auto_now=True),



