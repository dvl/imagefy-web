from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter as FacebookOAuth2AdapterBase

from rest_auth.registration.views import SocialLoginView


class FacebookOAuth2Adapter(FacebookOAuth2AdapterBase):
    def __init__(self):
        pass


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
