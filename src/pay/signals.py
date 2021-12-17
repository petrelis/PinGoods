from django.shortcuts import get_object_or_404
from .models import Subscription, SubscriptionOrder
from goods.models import Order
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.http import Http404


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        
        try:
            order = SubscriptionOrder.objects.get(id=ipn.invoice)
            subscription = get_object_or_404(Subscription, order=order.id)
        except SubscriptionOrder.DoesNotExist:
            try:
                for i in Order.objects.all():
                    key = str(0) + str(i.offer.id) + str(i.id)
                    if key == ipn.invoice:
                        order = i
            except Order.DoesNotExist:
                raise Http404("No order matches the given query.")
        
        if order.total_cost() == ipn.mc_gross:
            # mark the order as paid
            order.paid = True
            order.save()
            
            try:
                subscription
            except NameError:
                print ("ignore")
            else:
                subscription.valid = True
                subscription.save()
            