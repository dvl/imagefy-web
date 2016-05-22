from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from imagefy.profile.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

    fieldsets = (
        (_('Personal'), {
            'fields': (
                'type',
            )
        }),
    )

    verbose_name_plural = _('User\'s Information')


class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInline
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
