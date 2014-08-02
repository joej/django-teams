from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import *


class PersonAttributeInline(admin.TabularInline):
    model = PersonAttribute
    list_display = ('email', 'birthdate', 'height', 'weight')


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1
    list_display = ('squad', 'person', 'number')
    raw_id_fields = ('person',)
    filter_horizontal = ('positions', )


class StaffInline(admin.TabularInline):
    model = Staff
    extra = 1
    list_display = ('squad', 'person', 'function')
    raw_id_fields = ('person',)


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
    list_display = ('person', 'value', 'sortorder')
    raw_id_fields = ('person',)


class ResultInline(admin.TabularInline):
    model = RemoteResult
    extra = 1
    list_display = ('name', )


class TeamAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/WYMEditor/jquery/jquery.js',
            '/static/WYMEditor/wymeditor/jquery.wymeditor.pack.js',
            '/static/WYMEditor/wymeditor/admin_textarea.js')
        css = {
            "all": ("/static/WYMEditor/wymeditor/skins/default/skin.css",)
        }

    fieldsets = (
        (None, {
            'fields': (
                    ('name', 'slug'),
                    ('sortorder'),
                    'lastsquad'
                )
            }),
    )
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('slug', 'name', 'sortorder')
admin.site.register(Team, TeamAdmin)


class SquadAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/WYMEditor/jquery/jquery.js',
            '/static/WYMEditor/wymeditor/jquery.wymeditor.pack.js',
            '/static/WYMEditor/wymeditor/admin_textarea.js')
        css = {
            "all": ("/static/WYMEditor/wymeditor/skins/default/skin.css",)
        }

    fieldsets = (
        (None, {
            'fields': (
                    ('name', 'slug', 'team', 'season'),
                    ('sortorder'),
                    ('predecessor', 'successor'),
                )
            }),
    )
    inlines = (PlayerInline, StaffInline, ContactInline, ResultInline)
    #filter_horizontal = ('images', 'calendars')
    prepopulated_fields = {'slug': ('season', 'team', 'name')}
    list_display = ('slug', 'name', 'team', 'season', 'sortorder')
admin.site.register(Squad, SquadAdmin)


class TransferUpdateAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False # To remove the 'Save and continue editing' button
admin.site.register(TransferUpdate, TransferUpdateAdmin)


class SquadCopyAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False # To remove the 'Save and continue editing' button
admin.site.register(SquadPlayerCopy, SquadCopyAdmin)


class PersonalSponsorAdmin(admin.ModelAdmin):
    list_display = ('image', 'url', 'person')
admin.site.register(PersonalSponsor, PersonalSponsorAdmin)


class PersonAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/WYMEditor/jquery/jquery.js',
            '/static/WYMEditor/wymeditor/jquery.wymeditor.pack.js',
            '/static/WYMEditor/wymeditor/admin_textarea.js')
        css = {
            "all": ("/static/WYMEditor/wymeditor/skins/default/skin.css",)
        }

    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    fieldsets = (
        (None, {
            'fields': (
                ('first_name', 'last_name', 'slug'),
                'sortorder',
            )
        }),
    )
    inlines = (PersonAttributeInline, PlayerInline, StaffInline)
    search_fields = ('first_name', 'last_name')
    list_display = ('slug', 'first_name', 'last_name', 'sortorder')
admin.site.register(Person, PersonAdmin)


class RemoteResultAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(RemoteResult, RemoteResultAdmin)        


class DateAdmin(admin.ModelAdmin):
    list_display = ('datum', 'name')
admin.site.register(Date, DateAdmin)


class TransferAdmin(admin.ModelAdmin):
    raw_id_fields = ('person', )
    list_display = ('person', 'old', 'oldextern', 'new', 'newextern')
admin.site.register(Transfer, TransferAdmin)


class ExternalTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'url')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(ExternalTeam, ExternalTeamAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Position, PositionAdmin)


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Season, SeasonAdmin)


class TeamImageAdmin(admin.ModelAdmin):
    list_display = ('team', 'image', 'sort')
admin.site.register(TeamImage, TeamImageAdmin)


class SquadImageAdmin(admin.ModelAdmin):
    list_display = ('squad', 'image', 'sort')
admin.site.register(SquadImage, SquadImageAdmin)


class PersonImageAdmin(admin.ModelAdmin):
    list_display = ('person', 'image', 'sort')
admin.site.register(PersonImage, PersonImageAdmin)
