"""Applications hooks for teams.plugins"""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

#from teams.plugins.settings import APP_MENUS


class TeamsApphook(CMSApp):
    """Teamss Apphook"""
    name = _('Team App Hook')
    urls = ['teams.urls']
    #menus = APP_MENUS

apphook_pool.register(TeamsApphook)