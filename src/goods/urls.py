from django.urls import path
from . import views

app_name = "goods"


urlpatterns = [
    path("", views.Index.as_view(), name= "index"),
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("main", views.MainView, name= "main"),
    path("addoffer", views.AddOffer, name= "addoffer"),
    path("<int:offer_id>/addreview", views.AddReview, name= "addreview"),
    path("<int:offer_id>/editoffer", views.EditOffer, name= "editoffer"),
]