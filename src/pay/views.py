from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.conf import settings
from decimal import Decimal
from django.utils import timezone
from django.views import generic
from .models import Subscription, SubscriptionOrder
from .forms import CheckoutForm
from paypal.standard.forms import PayPalPaymentsForm

@login_required
def index(request):
    return render(request,'pay/index.html')



def checkout(request):
    if request.method == 'POST':
        o = SubscriptionOrder(
            name = request.user,
            email = "None",
            postal_code = 0,
            address = "None",
        )
        o.save()

        current_user = request.user
        date = datetime.now()
        li = Subscription(
            user=current_user,
            start_date=date,
            end_date=date+timedelta(days=30),
            order_id = o.id,
            valid = False)

        li.save()

        request.session['order_id'] = o.id

        messages.add_message(request, messages.INFO, 'Order Placed!')
        return redirect('/pay/process-payment')


    else:
        return render(request, 'pay/checkout.html')

def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(SubscriptionOrder, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.total_cost(),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('pay:payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('pay:payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'pay/process_payment.html', {'order': order, 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'pay/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'pay/payment_cancelled.html')