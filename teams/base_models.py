# coding=utf8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import get_model
from django.utils.html import linebreaks
from teams.settings import MARKUP_LANGUAGE
from teams.settings import MARKDOWN_EXTENSIONS

from django.contrib.markup.templatetags.markup import markdown
from django.contrib.markup.templatetags.markup import textile
from django.contrib.markup.templatetags.markup import restructuredtext


class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        """BaseModels's Meta"""
        abstract = True

    def __unicode__(self):
        return u'%s' % (self.name)


class PersonBase(models.Model):
    slug = models.SlugField()
    sortorder = models.SmallIntegerField(default=0)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    content = models.TextField(_('content'))

    class Meta:
        """Person's Meta"""
        abstract = True
        ordering = ['sortorder', 'slug']

    @property
    def html_content(self):
        """Return the content correctly formatted"""
        if MARKUP_LANGUAGE == 'markdown':
            return markdown(self.content, MARKDOWN_EXTENSIONS)
        elif MARKUP_LANGUAGE == 'textile':
            return textile(self.content)
        elif MARKUP_LANGUAGE == 'restructuredtext':
            return restructuredtext(self.content)
        elif not '</p>' in self.content:
            return linebreaks(self.content)
        return self.content

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class PersonAttributeBase(models.Model):
    person = models.OneToOneField('Person', related_name='attributes')
    email = models.EmailField(_('e-mail address'), blank=True)
    birthdate = models.DateField(blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField(blank=True, null=True)


class TeamBase(BaseModel):
    sortorder = models.SmallIntegerField(default=0)
    lastsquad = models.ForeignKey('Squad', blank=True, null=True, related_name='lastteam_set')

    class Meta:
        abstract = True
        verbose_name = 'team'
        verbose_name_plural = 'teams'
        ordering = ['sortorder', 'name']

    def __unicode__(self):
        return u'%s' % self.name


class SquadBase(BaseModel):
    sortorder = models.SmallIntegerField(default=0)
    predecessor = models.ForeignKey('self', related_name='predecessor_set', null=True, blank=True)
    successor = models.ForeignKey('self', related_name='successor_set', null=True, blank=True)
    team = models.ForeignKey('Team', null=True, related_name='squad_set')
    season = models.ForeignKey('Season')
    players = models.ManyToManyField('Person', related_name='player_squad', through='Player')
    staff = models.ManyToManyField('Person', related_name='staff_squad', through='Staff')
    contacts = models.ManyToManyField('Person', related_name='contact_squad', through='Contact')
    content = models.TextField(_('content'))

    class Meta:
        abstract = True
        verbose_name = 'squad'
        verbose_name_plural = 'squads'
        ordering = ['sortorder', 'name']
    # def save(self, *args, **kwargs):
    #     if self.predecessor == self:
    #         self.predecessor = None
    #     if self.successor == self:
    #         self.successor = None
    #     super(Squad, self).save(*args, **kwargs)
    #     if self.predecessor and self.predecessor.successor != self:
    #         self.predecessor.successor = self
    #         self.predecessor.save()
    #     if self.successor and self.successor.predecessor != self:
    #         self.successor.predecessor = self
    #         self.successor.save()
    #     last = self
    #     while not last.successor is None:
    #         last = last.successor
    #     last.team.lastsquad = last
    #     last.team.save()

    @property
    def html_content(self):
        """Return the content correctly formatted"""
        if MARKUP_LANGUAGE == 'markdown':
            return markdown(self.content, MARKDOWN_EXTENSIONS)
        elif MARKUP_LANGUAGE == 'textile':
            return textile(self.content)
        elif MARKUP_LANGUAGE == 'restructuredtext':
            return restructuredtext(self.content)
        elif not '</p>' in self.content:
            return linebreaks(self.content)
        return self.content

    def __unicode__(self):
        return u'%s - %s (%s)' % (self.team.name, self.name, self.season)


class DateBase(models.Model):
    datum = models.DateField()
    name = models.CharField(max_length=50, blank=True)

    class Meta:
        """DateBase's Meta"""
        abstract = True

    def __unicode__(self):
        if self.name:
            return u'%s | %s' % (self.name, self.datum)
        return u'%s' % (self.datum)


class SquadPerson(models.Model):
    person = models.ForeignKey('Person', related_name='%(app_label)s_%(class)s_person')
    squad = models.ForeignKey('Squad', related_name='%(app_label)s_%(class)s_squad')
    date_joined = models.ForeignKey('Date', related_name='%(app_label)s_%(class)s_date_joined', null=True, blank=True)
    date_left = models.ForeignKey('Date', related_name='%(app_label)s_%(class)s_date_left', null=True, blank=True)

    class Meta:
        abstract = True


class PlayerBase(SquadPerson):
    number = models.SmallIntegerField()
    positions = models.ManyToManyField('Position')

    class Meta:
        abstract = True
        ordering = ['squad', 'number', 'person']

    def __unicode__(self):
        return u'%s %s %d' % (self.squad, self.person, self.number)


class ContactBase(SquadPerson):
    sortorder = models.SmallIntegerField(default=0)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        abstract = True


class StaffBase(SquadPerson):
    sortorder = models.SmallIntegerField(default=0)
    function = models.CharField(max_length=50)

    class Meta:
        abstract = True
        ordering = ['squad', 'sortorder', 'person']

    def __unicode__(self):
        return u'%s %s %s' % (self.squad, self.person, self.function)
