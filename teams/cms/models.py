from django.db import models
from cms.models import CMSPlugin
from teams.models import Team, Player

class TeamPlugin(CMSPlugin):
    team = models.ForeignKey(Team)

class PlayerPlugin(CMSPlugin):
    player = models.ForeignKey(Player)