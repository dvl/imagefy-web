from django.contrib.auth import get_user_model

from rest_framework import serializers

from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from imagefy.wishes.models import Category, Offer, Wish


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
        ]


class OfferSerializer(serializers.ModelSerializer):
    salesman = UserSerializer()

    class Meta:
        model = Offer
        fields = [
            'shopify_product_id',
            'salesman',
            'created_at',
            'updated_at',
        ]


class WishSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = CategorySerializer()
    offers = OfferSerializer(many=True)
    owner = UserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = Wish
        fields = '__all__'
