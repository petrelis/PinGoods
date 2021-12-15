from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="first_name", help_text='Last Name')
    last_name = forms.CharField(max_length=100, label="last_name", help_text='Last Name')
    email = forms.EmailField(max_length=150, label="email", help_text='Email', required=False)
    phone = forms.CharField(max_length=15, label="phone", help_text='Phone', required=False)
    city = forms.CharField(max_length=30, label="city", help_text='City', required=False)
    address = forms.CharField(max_length=30, label="address", help_text='Address', required=False)
    iscustomer = forms.BooleanField(required=False)
    isseller = forms.BooleanField(required=False)

    class Meta:
          model = User
          fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 
                    'phone', 'city', 'address', 'iscustomer', 'isseller',)

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 
                  'phone', 'city', 'address', 'iscustomer', 'isseller',) 
        fields = ['username', 'email', 'phone', 'city', 'address'] 