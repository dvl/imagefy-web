from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
    )

    def get_avatar_url(self):
        return self.user.socialaccount_set.all()[0].get_avatar_url()
