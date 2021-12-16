import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.contrib import admin

class Category(models.Model): 
    category_name = models.CharField(max_length=50)
    category_colour = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    
    def __str__(self):
        return self.category_name


class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    offer_title = models.CharField(max_length=50)
    offer_text = models.CharField(max_length=1000, blank=True, null=True)
    offer_price = models.CharField(max_length=20, blank=True)
    offer_phonenumber = models.CharField(max_length=15, blank=True)
    offer_address = models.CharField(max_length=30, blank=True)
    offer_paypal = models.CharField(max_length=30, blank=True)
    offer_quantity = models.CharField(max_length=30, blank=True)
    pub_date = models.DateTimeField('date published')
    offer_coords_lat = models.FloatField(default=0)
    offer_coords_lng = models.FloatField(default=0)
    offer_image = models.ImageField(default='default.jpg', upload_to='offer_pics')
    active = models.BooleanField(default=True)
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
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    review_text = models.CharField(max_length=400)
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=now)
    def __str__(self):
        return self.review_text
    
class Order(models.Model):
    name = models.CharField(max_length=191)
    offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=191)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    def cost(self):
        return float(self.offer.offer_price)