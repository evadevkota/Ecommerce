from django.urls import path
from .views import index_page,open_signup_page, open_login_page,register,user_login, logout_user



urlpatterns = [
    path("index",index_page, name="index_page" ),
    path("open_signup_page",open_signup_page, name="open_signup"),
    path("open_login_page",open_login_page, name="open_login"),
    path("login",user_login,name="user_login"),
    path('register',register,name="register"),
    path('logout',logout_user,name="logout_user"),
 
  
      
]
