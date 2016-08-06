from django.conf.urls import patterns, url

from views import PersonDetail
from views import PositionDetail
from views import SquadList
from views import SquadDetail
from views import SeasonDetail
from views import SeasonList
from views import TeamList
from views import TeamDetail


urlpatterns = [
    url(r'^$', TeamList.as_view(), name='team_list'),
    url(r'^person/(?P<slug>[-\w]+)/$', PersonDetail.as_view(), name='team_person_detail'),
    url(r'^position/(?P<slug>[-\w]+)/$', PositionDetail.as_view(), name='position_detail'),
    url(r'^season/$', SeasonList.as_view(), name='season_list'),
    url(r'^season/(?P<slug>[-\w]+)$', SeasonDetail.as_view(), name='season_detail'),
    url(r'^squad/$', SquadList.as_view(), name='squad_list'),
    url(r'^squad/(?P<slug>[-\w]+)/$', SquadDetail.as_view(), name='squad_detail'),
    url(r'^team/(?P<slug>[-\w]+)/$', TeamDetail.as_view(), name='team_detail'),
]
