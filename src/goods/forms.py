from django import forms
from django.contrib.auth.models import User
from .models import Category, Offer

class OfferEditForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['category', 'description', 'phone_number', 'address', 'price']