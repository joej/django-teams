"""Admin of Teams CMS Plugins"""
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin
from teams.admin import PersonAdmin, SquadAdmin
from teams.models import Person, Squad

from django.utils.translation import ugettext_lazy as _


class PersonPlaceholderAdmin(PlaceholderAdminMixin, PersonAdmin):
    """PersonPlaceholder Admin"""
    pass

admin.site.unregister(Person)
admin.site.register(Person, PersonPlaceholderAdmin)

class SquadPlaceholderAdmin(PlaceholderAdminMixin, SquadAdmin):
    """SquadPlaceholder Admin"""
    pass

admin.site.unregister(Squad)
admin.site.register(Squad, SquadPlaceholderAdmin)
