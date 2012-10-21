from django.shortcuts import redirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import list_detail
from django.db.models.signals import post_save, post_delete
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.template import RequestContext
from models import Team, Squad, Person, Position, Player, Staff
from django.conf import settings

if settings.DEBUG:
    CACHETIME = 1
else:
    CACHETIME = 60 * 1 * 1 # 1 minute

@cache_page(CACHETIME, key_prefix='team_list')
def list(request):
    teams = Team.objects.order_by('sortorder')
    return list_detail.object_list(request, teams)

@cache_page(CACHETIME, key_prefix='team_detail')
def team_detail(request, team, **kwargs):
    return list_detail.object_detail(
        request, 
        queryset = Team.objects.all(), 
        slug = team, 
        **kwargs)
    
@cache_page(CACHETIME, key_prefix='squad_list')
def squad_list(request):
    squads = Squad.objects.order_by('sortorder')
    return list_detail.object_list(request, squads)

@cache_page(CACHETIME, key_prefix='squad_detail')
def squad_detail(request, squad, **kwargs):
    return list_detail.object_detail(
        request,
        queryset = Squad.objects.filter(slug=squad),
        slug = squad,
        extra_context = {
            'players': Player.objects.filter(squad__slug=squad).select_related(),
            'staffs': Staff.objects.select_related().filter(squad__slug=squad),
        },
        **kwargs)

@cache_page(CACHETIME, key_prefix='person_detail')
def person_detail(request, username, **kwargs):
    if request.is_ajax():
        return list_detail.object_detail(
            request,
            queryset = Person.objects.all(),
            slug_field = 'slug',
            slug = username,
            template_name = 'teams/person_detail_ajax.html',
            **kwargs
        )
    return list_detail.object_detail(
        request,
        queryset = Person.objects.all(),
        slug_field = 'slug',
        slug = username,
        **kwargs
    )
        
@cache_page(CACHETIME, key_prefix='position_detail')
def position_detail(request, position, **kwargs):
    return list_detail.object_detail(
        request,
        queryset = Position.objects.all().order_by('squad'),
        slug = position,
        **kwargs
    )

def expire_view_cache(view_name, kwargs={}, namespace=None, key_prefix=None, method="GET"):
    """
    This function allows you to invalidate any view-level cache. 
        view_name: view function you wish to invalidate or it's named url pattern
        args: any arguments passed to the view function
        namepace: optioal, if an application namespace is needed
        key prefix: for the @cache_page decorator for the function (if any)

        from: http://stackoverflow.com/questions/2268417/expire-a-view-cache-in-django
        added: method to request to get the key generating properly
    """
    from django.core.urlresolvers import reverse
    from django.http import HttpRequest
    from django.utils.cache import get_cache_key
    from django.core.cache import cache
    # create a fake request object
    request = HttpRequest()
    request.method = method
    # Loookup the request path:
    if namespace:
        view_name = namespace + ":" + view_name
    request.path = reverse(view_name, kwargs=kwargs)
    # get cache key, expire if the cached item exists:
    key = get_cache_key(request, key_prefix=key_prefix)
    if key:
        if cache.get(key):
            cache.set(key, None, 0)
        return True
    return False

def invalidate_cache(sender, **kwargs):
    expire_view_cache('team_list')
    expire_view_cache('team_detail', kwargs={'team': None})
    expire_view_cache('squad_list')
    expire_view_cache('squad_detail', kwargs={'squad': None})
    expire_view_cache('team_person_detail', kwargs={'username': None})
    expire_view_cache('position_detail', kwargs={'position': None})

post_save.connect(invalidate_cache, sender=Team)
post_delete.connect(invalidate_cache, sender=Team)

person_detail.__doc__ = list_detail.object_detail.__doc__
