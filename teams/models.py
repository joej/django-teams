# coding=utf8

from cms.models.fields import PlaceholderField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % (self.name)


class Active(models.Model):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ImageModel(models.Model):
    images = models.ManyToManyField('Image', blank=True, related_name='%(app_label)s_%(class)s_image')

    class Meta:
        abstract = True

    def filter_query(self):
        return Image.objects.filter(image=self)

    def first_image(self):
        try:
            return self.filter_query().order_by('sort')[0].image
        except IndexError:
            return None

    def __unicode__(self):
        return u'%s' % (self.name)


class Image(models.Model):
    image = FilerImageField(null=False, blank=False)
    sort = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["sort"]

    def __unicode__(self):
        return u'%s | %s' % (self.image, self.sort)


def instance_placeholder(instance):
    return 'placeholder_%s' % (instance.__class__.__name__.lower())

class Placeholder(models.Model):
    placeholder = PlaceholderField(instance_placeholder)

    class Meta:
        abstract = True


class SquadPerson(models.Model):
    person = models.ForeignKey('Person', related_name='%(app_label)s_%(class)s_person')
    sortorder = models.SmallIntegerField(default=0)
    squad = models.ForeignKey('Squad', related_name='%(app_label)s_%(class)s_squad')

    class Meta:
        ordering = ['sortorder']


class Player(SquadPerson):
    number = models.SmallIntegerField()
    positions = models.ManyToManyField('Position')

    class Meta:
        ordering = ['number', 'sortorder', 'person']

    def position_part_list(self):
        seen = set()
        seen_add = seen.add
        result = []
        for p in self.positions.all():
            for x in p.name.split(' '):
                if x not in seen and not seen_add(x):
                    result.append(x)
        return result

    def __unicode__(self):
        return u'%s %s %d' % (self.squad, self.person, self.number)


class Contact(SquadPerson):
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)


class Staff(SquadPerson):
    function = models.CharField(max_length=50)

    class Meta:
        ordering = ['sortorder', 'person']

    def __unicode__(self):
        return u'%s %s %s' % (self.squad, self.person, self.function)


class Position(BaseModel):
    pass

    class Meta:
        pass


class PersonalSponsor(models.Model):
    image = FilerImageField(null=True, blank=True)
    url = models.URLField()
    person = models.ForeignKey('Person')


class Person(ImageModel, Placeholder):
    content = models.TextField(_('content'))
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    slug = models.SlugField()

    class Meta:
        """Person's Meta"""
        ordering = ['slug']

    def first_image(self):
        try:
            return Image.objects.filter(teams_person_image=self).order_by('sort')[0].image
        except IndexError:
            return None

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class PersonAttribute(models.Model):
    birthdate = models.DateField(blank=True, null=True)
    email = models.EmailField(_('e-mail address'), blank=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True)
    person = models.OneToOneField('Person', related_name='attributes')
    weight = models.PositiveSmallIntegerField(blank=True, null=True)


class Team(Active, BaseModel, ImageModel, Placeholder):
    lastsquad = models.ForeignKey('Squad', blank=True, null=True, related_name='lastteam_set')
    sortorder = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'
        ordering = ['sortorder', 'slug']

    def __unicode__(self):
        return u'%s' % self.name

    def filter_query(self):
        return Image.objects.filter(teams_team_image=self)

    def seasons(self):
        return Season.objects.filter(squad__team=self).order_by('slug')


class Squad(Active, BaseModel, ImageModel, Placeholder):
    content = models.TextField(_('content'))
    contacts = models.ManyToManyField('Person', related_name="%(app_label)s_%(class)s_contact_related", through='Contact')
    players = models.ManyToManyField('Person', related_name="%(app_label)s_%(class)s_players_related", through='Player')
    predecessor = models.ForeignKey('self', related_name='predecessor_set', null=True, blank=True)
    season = models.ForeignKey('Season')
    shv_saison_id = models.CharField(max_length=5, blank=True)
    shv_group_id = models.CharField(max_length=5, blank=True)
    shv_team_id = models.CharField(max_length=5, blank=True)
    sortorder = models.SmallIntegerField(default=0)
    staff = models.ManyToManyField('Person', related_name="%(app_label)s_%(class)s_staff_related", through='Staff')
    successor = models.ForeignKey('self', related_name='successor_set', null=True, blank=True)
    team = models.ForeignKey('Team', null=True, related_name="%(app_label)s_%(class)s_related")

    class Meta:
        verbose_name = 'squad'
        verbose_name_plural = 'squads'
        ordering = ['team', 'season', 'sortorder', 'slug']

    def __unicode__(self):
        if self.team is None:
            return u'%s  - (%s)' % (self.name, self.season)
        elif self.team.name != self.name:
            return u'%s %s - (%s)' % (self.team.name, self.name, self.season)
        else:
            return u'%s - (%s)' % (self.name, self.season)

    def filter_query(self):
        return Image.objects.filter(teams_squad_image=self)

    def splayers(self):
        return Player.objects.filter(squad=self).order_by('number')

    def scontacts(self):
        return Contact.objects.filter(squad=self).order_by('sortorder')

    def sstaff(self):
        return Staff.objects.filter(squad=self).order_by('sortorder')

    def first_image(self):
        try:
            return Image.objects.filter(squad=self).\
                order_by('sort')[0].image
        except IndexError:
            return None


class Season(BaseModel):
    class Meta:
        verbose_name = 'season'
        verbose_name_plural = 'seasons'
        ordering = ['name', ]
