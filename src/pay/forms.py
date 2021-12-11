from django import forms
from .models import SubscriptionOrder


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = SubscriptionOrder
        exclude = ('paid',)

        widgets = {
            'address': forms.Textarea(attrs={'row': 5, 'col': 8}),
        }