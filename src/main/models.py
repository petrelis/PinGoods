import datetime
from django.utils import timezone, formats

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pay.models import Subscription

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30, blank=True)
    iscustomer = models.BooleanField(default=False)
    isseller = models.BooleanField(default=False)
    issubscribed = models.BooleanField(default=False) #DO NOT USE, USE SUBSCRIBED INSTEAD
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return self.user.username
    
    def subscribed(self):
        result = False
        now = timezone.now()
        subscriptions = Subscription.objects.all()
        if subscriptions.filter(
                valid=True, 
                start_date__lte = now, 
                end_date__gte = now,
                user=self.user).exists():
            result=True
        
        return result
    
    def subscriptionenddate(self):
        now = timezone.now()
        subscriptions = Subscription.objects.all()
        if subscriptions.filter(
                valid=True, 
                start_date__lte = now, 
                end_date__gte = now,
                user=self.user).exists():
            result=subscriptions.filter(
                    valid=True, 
                    start_date__lte = now, 
                    end_date__gte = now,
                    user=self.user)
            
        return result[0].end_date
        

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()