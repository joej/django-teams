from django.template import Library
from easy_thumbnails.templatetags import thumbnail

register = Library()    

@register.tag(name="easy_thumbnail")
def easy_thumbnail(parser, token):
    return thumbnail.thumbnail(parser, token)
