from django.urls import path
from . import views

app_name = "goods"   


urlpatterns = [
    path("", views.Index.as_view(), name= "index"),
    path("addoffer", views.AddOffer, name= "addoffer"),
]