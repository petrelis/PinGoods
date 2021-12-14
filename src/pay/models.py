import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.contrib import admin
    
class Order(models.Model):
    name = models.CharField(max_length=191)
    email = models.EmailField()
    postal_code = models.IntegerField()
    address = models.CharField(max_length=191)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    def total_cost(self):
        return 10.00

class SubscriptionOrder(models.Model):
    name = models.CharField(max_length=191)
    email = models.EmailField() #Irrelevant
    postal_code = models.IntegerField() #Irrelevant
    address = models.CharField(max_length=191) #Irrelevant
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    def total_cost(self):
        return 5.00
    
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(SubscriptionOrder, on_delete=models.CASCADE, unique=True)
    start_date = models.DateTimeField('date bought')
    end_date = models.DateTimeField('date expired')
    valid = models.BooleanField(default=False)