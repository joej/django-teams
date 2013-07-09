"""Admin of Teams CMS Plugins"""
from django.contrib import admin
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from cms.plugin_rendering import render_placeholder
from cms.admin.placeholderadmin import PlaceholderAdmin

from teams.models import Person, Squad
from teams.admin import PersonAdmin, SquadAdmin
from teams.settings import PERSON_BASE_MODEL, SQUAD_BASE_MODEL

class PersonPlaceholderAdmin(PlaceholderAdmin, PersonAdmin):
    """PersonPlaceholder Admin"""
    fieldsets = ((None, {'fields': (('first_name', 'last_name', 'slug'), 'sortorder',)}),
 #                (_('Content'), {'fields': ('content_placeholder',),
 #                        'classes': ('plugin-holder',
 #                                    'plugin-holder-nopage')}),
    )
    
    def save_model(self, request, person, form, change):
        """Fill the content field with the interpretation
        of the placeholder"""
        context = RequestContext(request)
        person.content = render_placeholder(person.content_placeholder, context)
        super(PersonPlaceholderAdmin, self).save_model(
            request, person, form, change)

admin.site.unregister(Person)
admin.site.register(Person, PersonPlaceholderAdmin)

class SquadPlaceholderAdmin(PlaceholderAdmin, SquadAdmin):
    """SquadPlaceholder Admin"""
    fieldsets = (        (None, {
            'fields': (
                    ('name', 'slug', 'team', 'season'),
                    ('sortorder'),
                    ('predecessor', 'successor'),
                )
            }),

#                 (_('Content'), {'fields': ('content_placeholder',),
#                         'classes': ('plugin-holder',
#                                     'plugin-holder-nopage')}),
    )
    prepopulated_fields = {'slug': ('name',)}
    
    def save_model(self, request, squad, form, change):
        """Fill the content field with the interpretation
        of the placeholder"""
        context = RequestContext(request)
        squad.content = render_placeholder(squad.content_placeholder, context)
        super(SquadPlaceholderAdmin, self).save_model(
            request, squad, form, change)

admin.site.unregister(Squad)
admin.site.register(Squad, SquadPlaceholderAdmin)
