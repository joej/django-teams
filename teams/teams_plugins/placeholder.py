"""Placeholder models for Teams"""
import inspect

from cms.models.fields import PlaceholderField
from cms.plugin_rendering import render_placeholder

from teams.base_models import PersonBase
from teams.base_models import SquadBase


class PersonPlaceholder(PersonBase):
    """Person with a Placeholder to edit content"""

    content_placeholder = PlaceholderField('content')

    def acquire_context(self):
        """
        Inspect the stack to acquire the current context used,
        to render the placeholder. I'm really sorry for this,
        but if you have a better way, you are welcome !
        """
        frame = None
        try:
            for f in inspect.stack()[1:]:
                frame = f[0]
                args, varargs, keywords, alocals = inspect.getargvalues(frame)
                if 'context' in args:
                    return alocals['context']
        finally:
            del frame

    @property
    def html_content(self):
        """No additional formatting is necessary"""
        context = self.acquire_context()
        return render_placeholder(self.content_placeholder, context)

    class Meta:
        """PersonPlaceholder's Meta"""
        abstract = True


class SquadPlaceholder(SquadBase):
    """Squad with a Placeholder to edit content"""

    content_placeholder = PlaceholderField('content')

    def acquire_context(self):
        """
        Inspect the stack to acquire the current context used,
        to render the placeholder. I'm really sorry for this,
        but if you have a better way, you are welcome !
        """
        frame = None
        try:
            for f in inspect.stack()[1:]:
                frame = f[0]
                args, varargs, keywords, alocals = inspect.getargvalues(frame)
                if 'context' in args:
                    return alocals['context']
        finally:
            del frame

    @property
    def html_content(self):
        """No additional formatting is necessary"""
        context = self.acquire_context()
        return render_placeholder(self.content_placeholder, context)

    class Meta:
        """SquadPlaceholder's Meta"""
        abstract = True
