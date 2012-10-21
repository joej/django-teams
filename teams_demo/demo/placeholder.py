"""Placeholder models for Teams"""
from teams.base_models import PersonBase
from teams.base_models import SquadBase


class PersonPlaceholder(PersonBase):
    """Person with a Placeholder to edit content"""

    @property
    def html_content(self):
        """No additional formatting is necessary"""
        return self.content

    class Meta:
#        def __init__(self, *args, **kwargs):
#            super(Meta, self).__init__()
        """PersonPlaceholder's Meta"""
        abstract = True


class SquadPlaceholder(SquadBase):
    """Squad with a Placeholder to edit content"""

    @property
    def html_content(self):
        """No additional formatting is necessary"""
        return self.content

    class Meta:
        """SquadPlaceholder's Meta"""
        abstract = True
