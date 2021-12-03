from django urls import path
from . import views

urlpatterns= [
    path ('', views.home, name='home' ),
    path('createpost/', views.createpost, name='home'),
    path ('uploadpost/', views.uploadpost, name='uploadpost'),
    path ('searchbar/', views.searchbar, name='searchbar'),
    path ('<slug>', views.details, name='details'),
    path (' ', views.PostIndexViews.as_view(), name='post-list'),
    path ('detail/ <int:pk>', views.PostIndexViews.as_view(), name 'post_detail'),
    path ('searchbar/', views.BlogSearchView.as_view(), name ='searchbar')
]