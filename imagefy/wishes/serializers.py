from rest_framework import serializers

from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from imagefy.wishes.models import Category, Offer, Wish
from imagefy.profile.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
        ]


class OfferSerializer(serializers.ModelSerializer):
    salesman = UserSerializer()

    class Meta:
        model = Offer
        exclude = [
            'id',
            'wish'
        ]


class WishSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = CategorySerializer()
    offers = OfferSerializer(many=True)
    owner = UserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = Wish
        fields = '__all__'
