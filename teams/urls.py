from django.conf.urls.defaults import *
from teams import views as team_views

urlpatterns = patterns('teams.views',
    url(r'^$', 'list', name='team_list'),
    url(r'^team/(?P<team>[-\w]+)/$', 'team_detail', name='team_detail'),
    url(r'^squad/$', 'squad_list', name='squad_list'),
    url(r'^squad/(?P<squad>[-\w]+)/$', 'squad_detail', name='squad_detail'),
    url(r'^person/(?P<username>[-\w]+)/$', 'person_detail', name='team_person_detail'),
    url(r'^position/(?P<position>[-\w]+)/$', 'position_detail', name='position_detail'),
)