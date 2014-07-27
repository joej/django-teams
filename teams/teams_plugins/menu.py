from cms.menu_bases import CMSAttachMenu
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from teams.models import Team

class TeamMenu(CMSAttachMenu):

    name = _("Team menu")

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for team in Team.objects.all():
            if team.lastsquad is None:
                node = NavigationNode(
                    team.name,
                    reverse('teams:team_detail', args=(team.slug, )),
                    team.slug)
            else:
                node = NavigationNode(
                    team.name,
                    reverse('teams:squad_detail', args=(team.lastsquad.slug, )),
                    team.lastsquad.slug)
            nodes.append(node)
        return nodes

menu_pool.register_menu(TeamMenu)
