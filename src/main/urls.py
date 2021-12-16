from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import MyPasswordChangeView, MyPasswordResetDoneView
from django.urls import reverse_lazy

app_name = "main"   


urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("home", views.home_page, name="homepage"),
    path("<int:pk>/", views.ProfileView.as_view(), name='profile'),
    path("register", views.registrationchoice_page, name="registrationchoice"),
    path("register/seller", views.sellerregister_page, name="sellerregister"),
    path("register/customer", views.customerregister_page, name="customerregister"),
    path("edit_profile", views.usereditview_page, name="edit_profile"),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_page, name= "logout"),
    path('change-password/', MyPasswordChangeView.as_view(success_url='done'), name='password-change-view'),
    path('change-password/done/', views.MyPasswordResetDoneView, name='password_change_done'),
]