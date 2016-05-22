from django.contrib import admin

from imagefy.wishes.models import Offer, Wish


class OfferInline(admin.StackedInline):
    model = Offer
    extra = 0


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    inlines = (OfferInline,)
    list_display = ('pk', 'brief', 'budget', 'created_at', 'updated_at')
