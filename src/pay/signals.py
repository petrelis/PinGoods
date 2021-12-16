from django.shortcuts import get_object_or_404
from .models import Subscription, SubscriptionOrder
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from datetime import datetime, timedelta
from django.contrib.auth.models import User


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        
        # payment was successful
        order = get_object_or_404(SubscriptionOrder, id=ipn.invoice)
        subscription = get_object_or_404(Subscription, order=order.id)
        
        print(order.id)
        print(subscription.id)

        if order.total_cost() == ipn.mc_gross:
            # mark the order as paid
            order.paid = True
            subscription.valid = True
            order.save()
            subscription.save()
            