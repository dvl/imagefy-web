from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.authtoken import views as rest_views

from imagefy.api import router
from imagefy.core.views import FacebookLogin


urlpatterns = [
    url(r'^api/v1/', include(router.urls)),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^api/v1/docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', admin.site.urls),
]
