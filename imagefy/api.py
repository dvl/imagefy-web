from rest_framework import routers

from imagefy.wishes.views import OfferViewSet, WishViewSet

router = routers.SimpleRouter()
router.register(r'wishes', WishViewSet)
router.register(r'offers', OfferViewSet)
