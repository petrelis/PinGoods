from django.contrib import admin
from goods.models import Offer, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class OfferAdmin(admin.ModelAdmin):
    list_display = ('offer_title', 'user', 'offer_category', 'pub_date', 'was_published_recently')
    inlines = [ReviewInline]

admin.site.register(Offer, OfferAdmin)