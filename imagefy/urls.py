from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework.authtoken import views as rest_views

from imagefy.core.views import FacebookLogin


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
    url(r'^api/v1/', include('rest_auth.urls')),
    url(r'^api/v1/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/registration/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^api/v1/registration/auth-token/', rest_views.obtain_auth_token),
    url(r'^admin/', admin.site.urls),
]
