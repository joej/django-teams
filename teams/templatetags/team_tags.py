from django import template
from easy_thumbnails.files import get_thumbnailer
from django.utils.html import escape

register = template.Library()

@register.tag(name="person_squad_image")
def do_person_squad_image(parser, token):
    try:
        tag_name, person, squad = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly two arguments, (Person and Squad object)" % token.contents.split()[0])
    return PlayerSquadImage(person, squad)

from django import template
from teams.models import Person, Squad, SquadPersonImage
class PlayerSquadImage(template.Node):
    def __init__(self, person, squad):
        self.person = template.Variable(person)
        self.squad = template.Variable(squad)
    def render(self, context):
        image = None
        try:
            person = self.person.resolve(context)
            squad = self.squad.resolve(context)
        except template.VariableDoesNotExist:
            return ''
        try:
            image = SquadPersonImage.objects.get(person=person, squad=squad)
        except SquadPersonImage.DoesNotExist:
            pass
        opts = {}
        opts['size'] = (100,100)
        thumbnail = None
        if image:
            # image is a TeamImage
            if image.image and image.image.image:
                thumbnail = get_thumbnailer(image.image.image).get_thumbnail(opts)
        elif person.images.count() > 0:
            image = person.images.all()[0]
            thumbnail = get_thumbnailer(image.image).get_thumbnail(opts)
        if thumbnail:
            return '<img src="%s" />' % escape(thumbnail.url)
        return '<img src="/static/teams/default.png" />'
