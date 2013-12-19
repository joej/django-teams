from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from models import Team, Squad, Person, Position, Player, Staff


class TeamList(ListView):
    model = Team

    def get_query_set(self):
        return Team.objects.order_by('sortorder')


class TeamDetail(DetailView):
    model = Team

'''
def team_detail(request, team, **kwargs):
    return DetailView.as_view(
        request,
        queryset=Team.objects.all(),
        slug=team,
        **kwargs)
'''


class SquadList(ListView):
    model = Squad

    def get_query_set(self):
        return Squad.objects.order_by('sortorder')


class SquadDetail(DetailView):
    model = Squad

    def get_context_data(self, **kwargs):
        context = super(SquadDetail, self).get_context_data(**kwargs)
        context['players'] = Player.objects.filter(squad__slug=self.object.slug).select_related()
        context['staffs'] = Staff.objects.filter(squad__slug=self.object.slug).select_related()
        return context


class PersonDetail(DetailView):
    model = Person


class PositionDetail(DetailView):
    model = Position

    def get_query_set(self):
        return Position.objects.order_by('squad')
