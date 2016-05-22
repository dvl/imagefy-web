from django.contrib.auth import get_user_model

from rest_framework import serializers

from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from imagefy.wishes.models import Category, Offer, Wish


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    salesman = UserSerializer()

    class Meta:
        model = Offer
        fields = '__all__'


class WishSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = CategorySerializer()
    offers = OfferSerializer(many=True)
    owner = UserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = Wish
        fields = '__all__'
