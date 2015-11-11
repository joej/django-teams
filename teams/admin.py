from django.contrib import admin
from django.forms.models import ModelForm
from models import Contact
from models import Image
from models import Person
from models import PersonalSponsor
from models import PersonAttribute
from models import Player
from models import Position
from models import Season
from models import Squad
from models import Staff
from models import Team


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


class TeamForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['lastsquad'].queryset = Squad.objects.filter(team=self.instance)


class TeamAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':
                (
                    ('name', 'slug'),
                    ('sortorder'),
                    'lastsquad',
                    'images'
                )
            }),
    )
    filter_horizontal = ('images',)
    form = TeamForm
    list_display = ('slug', 'name', 'sortorder')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Team, TeamAdmin)


class SquadForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SquadForm, self).__init__(*args, **kwargs)
        if not self.instance.team is None:
            self.fields['successor'].queryset = Squad.objects.filter(team=self.instance.team)
            self.fields['predecessor'].queryset = Squad.objects.filter(team=self.instance.team)


class SquadAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':
                (
                    ('name', 'slug', 'team', 'season'),
                    ('sortorder'),
                    ('shv_saison_id', 'shv_group_id', 'shv_team_id'),
                    ('predecessor', 'successor'),
                    'images'
                )
            }),
    )
    filter_horizontal = ('images', )
    form = SquadForm
    inlines = (PlayerInline, StaffInline, ContactInline)
    list_display = ('slug', 'name', 'team', 'season', 'sortorder')
    list_filter = ('season', 'team')
    prepopulated_fields = {'slug': ('season', 'team', 'name')}
admin.site.register(Squad, SquadAdmin)


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
    inlines = (PersonAttributeInline, PersonalSponsorInline, PlayerInline, StaffInline)
    filter_horizontal = ('images',)
    search_fields = ('first_name', 'last_name')
admin.site.register(Person, PersonAdmin)


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
