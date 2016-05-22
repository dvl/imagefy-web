from rest_framework import viewsets
from rest_framework_extensions import mixins

from imagefy.profile.models import Profile
from imagefy.wishes.models import Offer, Wish
from imagefy.wishes.serializers import OfferSerializer, WishSerializer


class WishViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.profile.type == Profile.SALESMAN:
            return qs

        return qs.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OfferViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def perform_update(self, serializer):
        serializer.save()
