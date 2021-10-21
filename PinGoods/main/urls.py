from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("home", views.home_page, name="homepage"),
    path("register", views.register_page, name="register"),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_page, name= "logout"),
]