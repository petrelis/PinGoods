from django.urls import path
from . import views

app_name = "goods"   


urlpatterns = [
    path("", views.Index.as_view(), name= "index"),
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("main", views.MainView, name= "main"),
    path("addoffer", views.AddOffer, name= "addoffer"),
    path("offerlist", views.OfferList.as_view(), name= "offerlist"),
    path("<int:offer_id>/addreview", views.AddReview, name= "addreview"),
    path("<int:offer_id>/editoffer", views.EditOffer, name= "editoffer"),
    path("<int:offer_id>/checkout", views.checkout, name= "checkout"),
    path("<int:offer_id>/process_payment", views.process_payment, name= "process_payment"),
    path('payment-done', views.payment_done, name='payment_done'),
    path('payment-cancelled', views.payment_canceled, name='payment_cancelled'),
]