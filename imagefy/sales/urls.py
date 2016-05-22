from django.conf.urls import url

from imagefy.sales.views import WishListView, WishDetailView, product_proxy

urlpatterns = [
    url(r'^$', WishListView.as_view(), name='list'),
    url(r'(?P<pk>\d+)/$', WishDetailView.as_view(), name='detail'),
    url(r'proxy/$', product_proxy, name='proxy'),
]
