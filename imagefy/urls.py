from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from imagefy.api import router
from imagefy.core.views import FacebookLogin, ShopifyLogin


urlpatterns = [
    url(r'^api/v1/', include(router.urls)),

    url(r'^api/v1/auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/auth/facebook/$', FacebookLogin.as_view(), name='facebook_login'),
    url(r'^api/v1/auth/shopify/$', ShopifyLogin.as_view(), name='shopify_login'),
    url(r'^api/v1/auth/', include('rest_auth.urls')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^sales/', include('imagefy.sales.urls', namespace='sales')),

    url(r'^api/v1/docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
