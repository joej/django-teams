from django.contrib import admin

from models import *

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
    list_display = ('person', 'value', 'sortorder')
    raw_id_fields = ('person',)


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


class PersonalSponsorInline(admin.TabularInline):
    model = PersonalSponsor
    extra = 1
    list_display = ('image', 'url', 'person')
    raw_id_fields = ('person',)


class TeamAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                    ('name', 'slug'),
                    ('sortorder'),
                    'lastsquad',
                    'images'
                )
            }),
    )
    filter_horizontal = ('images',)
    list_display = ('slug', 'name', 'sortorder')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Team, TeamAdmin)


class SquadAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                    ('name', 'slug', 'team', 'season'),
                    ('sortorder'),
                    ('predecessor', 'successor'),
                    'images'
                )
            }),
    )
    filter_horizontal = ('images', )
    inlines = (PlayerInline, StaffInline, ContactInline)
    list_display = ('slug', 'name', 'team', 'season', 'sortorder')
    list_filter = ('season', 'team')
    prepopulated_fields = {'slug': ('season', 'team', 'name')}
admin.site.register(Squad, SquadAdmin)


#class PersonalSponsorAdmin(admin.ModelAdmin):
#    list_display = ('image', 'url', 'person')
#admin.site.register(PersonalSponsor, PersonalSponsorAdmin)


class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    fieldsets = (
        (None, {
            'fields': (
                ('first_name', 'last_name', 'slug'),
                'images'
            )
        }),
    )
    list_display = ('slug', 'first_name', 'last_name')
    inlines = (PersonAttributeInline, PlayerInline, StaffInline)
    filter_horizontal = ('images',)
    search_fields = ('first_name', 'last_name')
admin.site.register(Person, PersonAdmin)


class DateAdmin(admin.ModelAdmin):
    list_display = ('datum', 'name')
admin.site.register(Date, DateAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Position, PositionAdmin)


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Season, SeasonAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'sort')
admin.site.register(Image, ImageAdmin)
