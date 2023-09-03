from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

        
# Create your views here.

# index page
def index_page(request):
    return render(request,'index.html')
    
# signup page
def open_signup_page(request):
    return render(request,'signup.html')
#register the user
def register(request):
    if request.method == 'POST':
        # get frontend username and password
        username = request.POST['username']
        password = request.POST['password']
        email= request.POST['email']
        print(username, password,email)

        # Checking if the user exists in database
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists!')
        else:
            User.objects.create(username=username,password=password,email=email)
            # user create
            messages.info(request, 'User created Successfully!')
            
    else:
        print("This is not POST method")
    return render(request,"signup.html")

#open user login page
def open_login_page(request):
    return render(request,"login.html")
# user login
def user_login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        print(username,password)
        # checking if user exists in database

        if User.objects.filter(username=username).exists():
            # login here
            user= User.objects.get(username=username)
            login(request,user)
            return redirect('open_men_collection')
        else:
            messages.error(request,"No such username or password")
    else:
        print("this is not post method")
    return render(request,'signup.html')
@login_required
#user logout
def logout_user(request):
    logout(request)
    return redirect("open_login")

