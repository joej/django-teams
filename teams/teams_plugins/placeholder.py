"""Placeholder models for Teams"""
from cms.models.fields import PlaceholderField

from django.db import models
from teams.base_models import PersonBase
from teams.base_models import SquadBase

class PersonPlaceholder(PersonBase):
    """Person with a Placeholder to edit content"""

    content_placeholder = PlaceholderField('content')

    @property
    def html_content(self):
        """No additional formatting is necessary"""
        return self.content

    class Meta:
        """PersonPlaceholder's Meta"""
        abstract = True

class SquadPlaceholder(SquadBase):
    """Squad with a Placeholder to edit content"""

    content_placeholder = PlaceholderField('content')

    @property
    def html_content(self):
        """No additional formatting is necessary"""
        return self.content

    class Meta:
        """SquadPlaceholder's Meta"""
        abstract = True
