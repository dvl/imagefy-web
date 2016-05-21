from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.authtoken import views as rest_views

from imagefy.core.views import FacebookLogin


urlpatterns = [
    url(r'^api/v1/', include('rest_auth.urls')),
    url(r'^api/v1/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/registration/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^api/v1/registration/auth-token/', rest_views.obtain_auth_token),
    url(r'^api/v1/docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', admin.site.urls),
]
