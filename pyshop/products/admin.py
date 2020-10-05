from django.contrib import admin
from .models import Product, Offer, UserProfile


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("image", "videoTime", "icon", "title", "username", "views", "uploadeDay")

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user","icon")


admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Offer, OfferAdmin)
