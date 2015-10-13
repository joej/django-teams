from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _

from models import TeamPlugin, PlayerPlugin


class CMSTeamPlugin(CMSPluginBase):
    model = TeamPlugin
    name = _('Teams')
    render_template = 'cms/plugins/team.html'
    
    def render(self, context, instance, placeholder):
        context.update({'object':instance.team,
                        'placeholder':placeholder})
        return context
    
plugin_pool.register_plugin(CMSTeamPlugin)
