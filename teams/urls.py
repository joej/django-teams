from django.conf.urls import patterns, url

from teams.views import PersonDetail
from teams.views import PositionDetail
from teams.views import SquadList
from teams.views import SquadDetail
from teams.views import SeasonDetail
from teams.views import SeasonList
from teams.views import TeamList
from teams.views import TeamDetail


urlpatterns = patterns('teams.views',
    url(r'^$', TeamList.as_view(), name='team_list'),
    url(r'^person/(?P<slug>[-\w]+)/$', PersonDetail.as_view(), name='team_person_detail'),
    url(r'^position/(?P<slug>[-\w]+)/$', PositionDetail.as_view(), name='position_detail'),
    url(r'^season/$', SeasonList.as_view(), name='season_list'),
    url(r'^season/(?P<slug>[-\w]+)$', SeasonDetail.as_view(), name='season_detail'),
    url(r'^squad/$', SquadList.as_view(), name='squad_list'),
    url(r'^squad/(?P<slug>[-\w]+)/$', SquadDetail.as_view(), name='squad_detail'),
    url(r'^team/(?P<slug>[-\w]+)/$', TeamDetail.as_view(), name='team_detail'),
)
