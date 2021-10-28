from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("home", views.home_page, name="homepage"),
    path("register", views.registrationchoice_page, name="registrationchoice"),
    path("register/seller", views.sellerregister_page, name="sellerregister"),
    path("register/customer", views.customerregister_page, name="customerregister"),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_page, name= "logout"),
]