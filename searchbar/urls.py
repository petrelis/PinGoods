urlpatterns= [
    path ('', views.home, name='home' ),
    path('createpost/', views.createpost, name='home'),
    path ('uploadpost/', views.uploadpost, name='uploadpost'),
    path ('searchbar/', views.searchbar, name='searchbar'),
    path ('<slug>', views.details, name='details'),
]