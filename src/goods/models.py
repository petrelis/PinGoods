import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib import admin

#class Category(models.Model): 
    #(so customers can assign a category to an offer instead of writing it in)

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer_title = models.CharField(max_length=50)
    offer_text = models.CharField(max_length=500, blank=True)
    offer_category = models.CharField(max_length=50, blank=True)
    offer_price = models.CharField(max_length=20, blank=True)
    #offer_phonenumber = models.CharField(max_length=15, blank=True)
    #offer_address = models.CharField(max_length=30, blank=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.offer_title
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now

class Review(models.Model):
    question = models.ForeignKey(Offer, on_delete=models.CASCADE)
    #Review Author's Name
    review_text = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.review_text