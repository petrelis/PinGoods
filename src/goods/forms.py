from django import forms
from django.contrib.auth.models import User
from .models import Category, Offer

class OfferEditForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    paypal = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['title', 'text', 'category', 'quantity', 'phone_number', 'address', 'price', 'paypal', 'image'] 