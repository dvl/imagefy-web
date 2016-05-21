from django.contrib import admin

from imagefy.wishes.models import Category, Offer, Wish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class OfferInline(admin.StackedInline):
    model = Offer
    extra = 0


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    inlines = (OfferInline,)
