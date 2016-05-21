from rest_framework import viewsets

from imagefy.wishes.models import Offer, Wish
from imagefy.wishes.serializers import OfferSerializer, WishSerializer


class WishViewSet(viewsets.ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
