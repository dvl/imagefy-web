from django.contrib.auth import get_user_model
from rest_framework import serializers

from imagefy.wishes.models import Category, Offer, Wish


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
        ]


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'first_name'
        ]


class WishSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    offers = OfferSerializer(many=True)
    owner = OwnerSerializer()

    class Meta:
        model = Wish
        fields = '__all__'
