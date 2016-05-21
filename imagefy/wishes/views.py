from rest_framework import viewsets
from rest_framework_extensions import mixins

from imagefy.wishes.models import Offer, Wish
from imagefy.wishes.serializers import OfferSerializer, WishSerializer


class WishViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer


class OfferViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
