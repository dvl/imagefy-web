from rest_framework import serializers

from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from imagefy.wishes.models import Offer, Wish
from imagefy.profile.serializers import UserSerializer


class OfferSerializer(serializers.ModelSerializer):
    salesman = UserSerializer()

    class Meta:
        model = Offer
        exclude = [
            'id',
            'wish'
        ]


class WishSerializer(TaggitSerializer, serializers.ModelSerializer):
    offers = OfferSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)
    tags = TagListSerializerField(required=False)

    class Meta:
        model = Wish
        fields = '__all__'
