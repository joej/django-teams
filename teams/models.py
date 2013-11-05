# coding=utf8

import logging

from django.db import models
from django.db.models.signals import post_save
from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _

from teams.base_models import BaseModel, PersonBase, PersonAttributeBase, TeamBase, SquadBase, DateBase, SquadPerson, PlayerBase, ContactBase, StaffBase

from settings import PERSON_BASE_MODEL, PERSON_ATTR_BASE_MODEL, TEAM_BASE_MODEL, SQUAD_BASE_MODEL, PLAYER_BASE_MODEL, CONTACT_BASE_MODEL, STAFF_BASE_MODEL, DATE_BASE_MODEL

from filer.fields.image import FilerImageField


FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT)
log = logging.getLogger('Models')


def get_class( kls ):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = import_module( module )
    for comp in parts[1:]:
        m = getattr(m, comp)            
    return m


def get_base_model(BASE_MODEL):
    """Determine the base Model to inherit in the
    Entry Model, this allows to overload it."""

    dot = BASE_MODEL.rindex('.')
    module_name = BASE_MODEL[:dot]
    class_name = BASE_MODEL[dot + 1:]
    try:
        _class = getattr(import_module(module_name), class_name)
        return _class
    except (ImportError, AttributeError):
        log.warning('%s cannot be imported' % BASE_MODEL)
    return get_class(BASE_MODEL)


class Position(BaseModel):
    def __unicode__(self):
        return u'%s' % (self.name)


class PersonImage(models.Model):
    person = models.ForeignKey('Person')
    image = FilerImageField(null=True, blank=True)
    sort = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["sort"]


class PersonalSponsor(models.Model):
    image = FilerImageField(null=True, blank=True)
    url = models.URLField()
    person = models.ForeignKey('Person')


class Person(get_base_model(PERSON_BASE_MODEL)):
    def first_image(self):
        try:
            return PersonImage.objects.filter(person=self).\
                order_by('sort')[0].image
        except IndexError:
            return None


class PersonAttribute(get_base_model(PERSON_ATTR_BASE_MODEL)):
    pass


class Team(get_base_model(TEAM_BASE_MODEL)):
    def first_image(self):
        try:
            return TeamImage.objects.filter(team=self).\
                order_by('sort')[0].image
        except IndexError:
            return None


class ExternalTeam(BaseModel):
    url = models.URLField(blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.name)


class Date(get_base_model(DATE_BASE_MODEL)):
    pass


class Player(get_base_model(PLAYER_BASE_MODEL)):
    pass


class Contact(get_base_model(CONTACT_BASE_MODEL)):
    pass


class RemoteResult(BaseModel):
    squad = models.ForeignKey('Squad', related_name='results_squad')
    code = models.TextField(null=True, blank=True)


class Staff(get_base_model(STAFF_BASE_MODEL)):
    pass


class Transfer(models.Model):
    person = models.ForeignKey(Person)
    old = models.ForeignKey('Squad', related_name='leaving', blank=True, null=True)
    oldextern = models.ForeignKey(ExternalTeam, related_name='leaving_ext', blank=True, null=True)
    new = models.ForeignKey('Squad', related_name='joining', blank=True, null=True)
    newextern = models.ForeignKey(ExternalTeam, related_name='joining_ext', blank=True, null=True)
    class Meta:
        ordering = ['person']
    def _get_from(self):
        if not self.oldextern is None:
            return self.oldextern
        if self.old is None:
            return ''
        return self.old
    def _get_to(self):
        if not self.newextern is None:
            return self.newextern
        if self.new is None:
            return ''
        return self.new
    def __unicode__(self):
        return u'%s (%s - %s)' % (self.person, self.t_from, self.t_to)
    t_from = property(_get_from)
    t_to = property(_get_to)


class Squad(get_base_model(SQUAD_BASE_MODEL)):
    def transfer_in(self):
        return Transfer.objects.filter(new=self)
    def transfer_out(self):
        return Transfer.objects.filter(old=self)
    def splayers(self):
        return Player.objects.filter(squad=self).order_by('number')
    def scontacts(self):
        return Contact.objects.filter(squad=self).order_by('sortorder')
    def sstaff(self):
        return Staff.objects.filter(squad=self).order_by('sortorder')
    def first_image(self):
        try:
            return SquadImage.objects.filter(squad=self).\
                order_by('sort')[0].image
        except IndexError:
            return None


class Season(BaseModel):
    class Meta:
        verbose_name = 'season'
        verbose_name_plural = 'seasons'
        ordering = ['name', ]


class SquadPlayerCopy(models.Model):
    source = models.ForeignKey(Squad, related_name='source_copies')
    target = models.ForeignKey(Squad, related_name='target_copies')
    def process(self):
        for p in Player.objects.filter(squad=self.source):
            obj, created = Player.objects.get_or_create(person=p.person, 
                                    squad=self.target, 
                                    number=p.number)
            for pos in p.positions.all():
                obj.positions.add(pos)
            obj.save()
        for s in Staff.objects.filter(squad=self.source):
            obj, created = Staff.objects.get_or_create(person=s.person,
                                    squad=self.target,
                                    sortorder=s.sortorder,
                                    function=s.function)
        for c in Contact.objects.filter(squad=self.source):
            obj, created = Contact.objects.get_or_create(person=c.person,
                                    squad=self.target,
                                    sortorder=c.sortorder,
                                    address=c.address,
                                    phone=c.phone)


# signal for process_gallery and deletion
def trigger_process_squad_copy(sender, **kwargs):
    instance = kwargs.get('instance', None)
    if instance is not None:
        instance.process()
        instance.delete()

post_save.connect(trigger_process_squad_copy, sender=SquadPlayerCopy)


class TeamImage(models.Model):
    team = models.ForeignKey('Team')
    image = FilerImageField(null=True, blank=True)
    sort = models.IntegerField(default=0, db_index=True)


class SquadImage(models.Model):
    squad = models.ForeignKey('Squad')
    image = FilerImageField(null=True, blank=True)
    sort = models.IntegerField(default=0, db_index=True)


class TransferUpdate(models.Model):
    do_update = models.BooleanField('Delete all transfers and update them afterwards')
    def do_update(self):
        if self.do_update:
            for obj in Transfer.objects.all():
                obj.delete()
            for squad in Squad.objects.all():
                players = {}
                for p in squad.players.all():
                    players[p.slug] = p
                #person, newteam, oldteam
                pre = squad.predecessor
                if not pre is None:
                    for p in pre.players.all():
                        if p.slug in players:
                            del players[p.slug]
                        else:
                            # not found in current players -> transfer from oldteam
                            t, created = Transfer.objects.get_or_create(person=p, old=pre, new=None)
                    for pslug, p in players.items():
                        # remaining players not found in predecessor -> transfer to newteam
                        t, created = Transfer.objects.get_or_create(person=p, old=None, new=squad)
                suc = squad.successor
                if not suc is None:
                    for p in suc.players.all():
                        if p.slug in players:
                            del players[p.slug]
                        else:
                            # not found in current players -> transfer to successor
                            t, created = Transfer.objects.get_or_create(person=p, old=None, new=suc)
                    for pslug, p in players.items():
                        # remaining players not found in successor -> transfer from oldteam
                        t, created = Transfer.objects.get_or_create(person=p, old=squad, new=None)
            # find transfers for same player with oldteam = None and newteam = None: TODO


# signal for process_gallery and deletion
def trigger_transfer_property(sender, **kwargs):
    instance = kwargs.get('instance', None)
    if instance is not None:
        instance.do_update()
        instance.delete()

post_save.connect(trigger_transfer_property, sender=TransferUpdate)
