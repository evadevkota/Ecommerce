from django.shortcuts import render,redirect
from .models import AddToCart,ProductBuyerInfo


from django.contrib.auth.decorators import login_required
from django.contrib import messages




@login_required
def create_cart(request):
    if request.method=="POST":
   
        # data - title description
        data_title = request.POST['title_values']
        data_price = request.POST['price_values']
        data_type = request.POST['type_values']
        data_category = request.POST['category_values']
        my_user = request.user


        print(data_title,data_price,data_type,data_category)
        AddToCart.objects.create(cart_title=data_title, cart_price=data_price, cart_type=data_type, cart_category=data_category, user=my_user)
        
        messages.info(request, f"{data_title} has been added to your cart.")


    return redirect(open_cart)
        
       
        
def open_cart(request):
  my_user= request.user
  mycart_list =AddToCart.objects.filter(user= my_user)
  data = {
        'mycart_list_show': mycart_list
    }
  print(data)
  return render(request, "cart.html", data)





@login_required
def delete_cart_method(request,id):
    
    obj = AddToCart.objects.get(id=id) 
    obj.delete()
    messages.info(request,f"cart has been deleted...")
    Data_list = AddToCart.objects.all()
    data = {
        'product_list_show':Data_list
    }
    
    return render(request,"cart.html",data)

def total_Price(request):
   
    my_user = request.user
    mycart_list = AddToCart.objects.filter(user=my_user)
    total_price = sum(item.cart_price for item in mycart_list)
    data = {
        'mycart_list_show': mycart_list,
        'total_price': total_price
    }
    print("Total Price:", total_price) 
    return render(request, "cart.html", data)

@login_required
def checkout(request):
    my_user = request.user
    total_price = 0  # Initialize total price to 0

    # Calculate the total price by iterating over items in the cart
    mycart_list = AddToCart.objects.filter(user=my_user)
    for item in mycart_list:
        total_price += item.cart_price

    # Create a ProductBuyerInfo instance and save it
    buyer_info = ProductBuyerInfo(user=my_user, total_price=total_price)
    buyer_info.save()

    # Clear the user's shopping cart
    mycart_list.delete()

    messages.info(request, "Checkout successful. Your order has been placed.")

    return redirect(open_cart)
