from django.contrib import admin
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("image", "videoTime", "icon", "title", "username", "views", "uploadeDay")


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
