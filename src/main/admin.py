from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from main.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'address', 'iscustomer', 'isseller' , 'subscribed' )

admin.site.register(Profile, ProfileAdmin)