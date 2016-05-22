from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.shopify.views import ShopifyOAuth2Adapter

from rest_auth.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class ShopifyLogin(SocialLoginView):
    adapter_class = ShopifyOAuth2Adapter
