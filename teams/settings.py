""" Settings of Teams """
from django.conf import settings


PAGINATION = getattr(settings, 'TEAMS_PAGINATION', 10)

PERSON_BASE_MODEL = getattr(settings, 'TEAM_PERSON_BASE_MODEL', 'teams.models.PersonBase')
PERSON_ATTR_BASE_MODEL = getattr(settings, 'TEAM_PERSON_ATTRITBUTE_BASE_MODEL', 'teams.models.PersonAttributeBase')
TEAM_BASE_MODEL = getattr(settings, 'TEAM_TEAM_BASE_MODEL', 'teams.models.TeamBase')
SQUAD_BASE_MODEL = getattr(settings, 'TEAM_SQUAD_BASE_MODEL', 'teams.models.SquadBase')
PLAYER_BASE_MODEL = getattr(settings, 'TEAM_PLAYER_BASE_MODEL', 'teams.models.PlayerBase')
CONTACT_BASE_MODEL = getattr(settings, 'TEAM_CONTACT_BASE_MODEL', 'teams.models.ContactBase')
STAFF_BASE_MODEL = getattr(settings, 'TEAM_STAFF_BASE_MODEL', 'teams.models.StaffBase')
DATE_BASE_MODEL = getattr(settings, 'TEAM_DATE_BASE_MODEL', 'teams.models.DateBase')
