# coding=utf8

from django.db import models
from filer.fields.image import FilerImageField
from django.utils.translation import ugettext_lazy as _

class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        """BaseModels's Meta"""
        abstract = True

    def __unicode__(self):
        return u'%s' % (self.name)


class ImageBaseModel(BaseModel):
    images = models.ManyToManyField('Image', blank=True)

    class Meta:
        """BaseModels's Meta"""
        abstract = True

    def first_image(self):
        try:
            return Image.objects.filter(team=self).order_by('sort')[0].image
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

class SquadPerson(models.Model):
    date_joined = models.ForeignKey('Date', related_name='%(app_label)s_%(class)s_date_joined', null=True, blank=True)
    date_left = models.ForeignKey('Date', related_name='%(app_label)s_%(class)s_date_left', null=True, blank=True)
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


class Person(models.Model):
    content = models.TextField(_('content'))
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    images = models.ManyToManyField('Image', blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    slug = models.SlugField()

    class Meta:
        """Person's Meta"""
        ordering = ['slug']

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class PersonAttribute(models.Model):
    birthdate = models.DateField(blank=True, null=True)
    email = models.EmailField(_('e-mail address'), blank=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True)
    person = models.OneToOneField('Person', related_name='attributes')
    weight = models.PositiveSmallIntegerField(blank=True, null=True)


class Team(ImageBaseModel):
    lastsquad = models.ForeignKey('Squad', blank=True, null=True, related_name='lastteam_set')
    sortorder = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'
        ordering = ['sortorder', 'slug']

    def __unicode__(self):
        return u'%s' % self.name

    def seasons(self):
        return Season.objects.filter(squad__team=self).order_by('slug')


class Date(models.Model):
    datum = models.DateField()
    name = models.CharField(max_length=50, blank=True)

    class Meta:
        """DateBase's Meta"""
        pass

    def __unicode__(self):
        if self.name:
            return u'%s | %s' % (self.name, self.datum)
        return u'%s' % (self.datum)


class Squad(ImageBaseModel):
    content = models.TextField(_('content'))
    contacts = models.ManyToManyField('Person', related_name="%(app_label)s_%(class)s_contact_related", through='Contact')
    players = models.ManyToManyField('Person', related_name="%(app_label)s_%(class)s_players_related", through='Player')
    predecessor = models.ForeignKey('self', related_name='predecessor_set', null=True, blank=True)
    season = models.ForeignKey('Season')
    shv_id = models.CharField(max_length=100, blank=True)
    sortorder = models.SmallIntegerField(default=0)
    staff = models.ManyToManyField('Person', related_name="%(app_label)s_%(class)s_staff_related", through='Staff')
    successor = models.ForeignKey('self', related_name='successor_set', null=True, blank=True)
    team = models.ForeignKey('Team', null=True, related_name="%(app_label)s_%(class)s_related")

    class Meta:
        verbose_name = 'squad'
        verbose_name_plural = 'squads'
        order_with_respect_to = 'team'
        ordering = ['team', 'season', 'sortorder', 'slug']

    def __unicode__(self):
        if self.team is None:
            return u'%s (%s)' % (self.name, self.season)
        else:
            return u'%s - %s (%s)' % (self.team.name, self.name, self.season)

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

