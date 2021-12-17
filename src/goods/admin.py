from django.contrib import admin
from goods.models import Offer, Review, Category, Order, Favourite

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class OfferAdmin(admin.ModelAdmin):
    list_display = ('offer_title', 'user', 'category', 'pub_date', 'was_published_recently', 'active')
    inlines = [ReviewInline]
    
class CategoryAdmin(admin.ModelAdmin):
        list_display = ('category_name', 'category_colour')
        
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'offer', 'paid')
    
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('offer', 'user')

admin.site.register(Offer, OfferAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Favourite, FavouriteAdmin)