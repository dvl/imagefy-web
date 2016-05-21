from rest_framework_extensions import routers

from imagefy.wishes.views import OfferViewSet, WishViewSet

router = routers.ExtendedSimpleRouter()

wishes_router = router.register(r'wishes', WishViewSet, base_name='wish')
wishes_router.register(r'offers', OfferViewSet, base_name='wishes-offer', parents_query_lookups=['wish__pk', 'offer'])
