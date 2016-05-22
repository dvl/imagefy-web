from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from imagefy.profile.models import Profile

# TODO: Se não for um registro via sociallogin vai dar problema


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)

        profile, _ = Profile.objects.get_or_create(user=user)
        profile.type = Profile.CUSTOMER

        if user.socialaccount_set.first().get_provider().id == 'shopify':
            profile.type = Profile.SALESMAN

        profile.save()
