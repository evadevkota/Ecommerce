

# Create your views here.
from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

from .models import  Category, Product



 
#add all the product whose category name= men
@login_required
def open_men_collection(request):
    category_name = "Men"
   
    category_obj = Category.objects.get(name=category_name)
    product_list = Product.objects.filter(category=category_obj)
    data = {
        'product_list_show': product_list
    }
    print(data)
    return render(request, "men.html", data)


#add all the profuct whose category= women
@login_required
def open_women_collection(request):
    category_name = "Women"
    category_obj = Category.objects.get(name=category_name)
    product_list = Product.objects.filter(category=category_obj)
    data = {
        'product_list_show': product_list
    }
    return render(request, "women.html", data)
    

# add selected products to the cart  
