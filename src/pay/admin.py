from django.contrib import admin
from .models import Subscription, SubscriptionOrder

class OrderAdmin (admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'paid']

class SubscriptionAdmin (admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'valid')

admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(SubscriptionOrder, OrderAdmin)