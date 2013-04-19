from django.conf.urls import patterns, url
from teams.views import TeamList, TeamDetail
from teams.views import SquadList, SquadDetail
from teams.views import PersonDetail, PositionDetail

urlpatterns = patterns('teams.views',
    url(r'^$', TeamList.as_view(), name='team_list'),
    url(r'^team/(?P<slug>[-\w]+)/$', TeamDetail.as_view(), name='team_detail'),
    url(r'^squad/$', SquadList.as_view(), name='squad_list'),
    url(r'^squad/(?P<slug>[-\w]+)/$', SquadDetail.as_view(), name='squad_detail'),
    url(r'^person/(?P<slug>[-\w]+)/$', PersonDetail.as_view(), name='team_person_detail'),
    url(r'^position/(?P<slug>[-\w]+)/$', PositionDetail.as_view(), name='position_detail'),
)
