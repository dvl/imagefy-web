import requests

from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from imagefy.wishes.models import Wish


class WishListView(ListView):
    model = Wish


class WishDetailView(DetailView):
    model = Wish
    context_object_name = 'wish'

    def get_shopify_access_token(self):
        socialaccounts = self.request.user.socialaccount_set.all()

        for account in socialaccounts:
            socialtokens = account.socialtoken_set.all()

            for token in socialtokens:
                if token.app.provider == 'shopify':
                    return token

        raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopify_access_token'] = self.get_shopify_access_token()

        return context


def product_proxy(request):
    headers = {
        'X-Shopify-Access-Token': request.META.get('HTTP_X_SHOPIFY_ACCESS_TOKEN')
    }

    response = requests.get('https://imagefy.myshopify.com/admin/products.json', headers=headers)

    if response.ok:
        return JsonResponse(response.json())

    response.raise_for_status()
