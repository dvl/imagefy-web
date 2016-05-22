from rest_framework import serializers

from imagefy.wishes.models import Offer, Wish
from imagefy.profile.serializers import UserSerializer


class OfferSerializer(serializers.ModelSerializer):
    salesman = UserSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'


class WishSerializer(serializers.ModelSerializer):
    offers = OfferSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Wish
        fields = '__all__'
