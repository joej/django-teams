"""Applications hooks for teams.plugins"""
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from menu import TeamMenu

from django.utils.translation import ugettext_lazy as _


#from teams.plugins.settings import APP_MENUS
class TeamsApp(CMSApp):
    """Teamss Apphook"""
    name = _('Team')
    urls = ['teams.urls']
    menus = [TeamMenu]

apphook_pool.register(TeamsApp)
