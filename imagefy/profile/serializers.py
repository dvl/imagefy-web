from django.contrib.auth import get_user_model

from rest_framework import serializers

from imagefy.profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = [
            'id',
            'user',
        ]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'profile',
            'profile_picture',
        ]

    def get_profile_picture(self, obj):
        try:
            return obj.socialaccount_set.all()[0].get_avatar_url()
        except IndexError:
            return None
