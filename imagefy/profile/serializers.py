from django.contrib.auth import get_user_model

from rest_framework import serializers

from imagefy.profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        exclude = [
            'id',
            'user',
        ]

    def get_avatar_url(self, obj):
        try:
            return obj.user.socialaccount_set.all()[0].get_avatar_url()
        except IndexError:
            return None


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'profile',
        ]
