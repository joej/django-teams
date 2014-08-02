from django.db import models

"""Placeholder models for Teams"""
from cms.models.fields import PlaceholderField
from teams.base_models import PersonBase, SquadBase


class PersonPlaceholder(PersonBase):
    """Person with a Placeholder to edit content"""
    content_placeholder = PlaceholderField('content')

    class Meta:
        app_label = 'teams'
        abstract = True


class SquadPlaceholder(SquadBase):
    """Squad with a Placeholder to edit content"""
    content_placeholder = PlaceholderField('content')

    class Meta:
        app_label = 'teams'
        abstract = True
