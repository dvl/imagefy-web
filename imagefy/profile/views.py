from django.views.generic import ListView

from imagefy.wishes.models import Wish


class WishListView(ListView):
    model = Wish
