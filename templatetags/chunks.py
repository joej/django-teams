# templatetags file
from django import template


register = template.Library()

@register.filter(name='chunks')
def chunks(iterable, chunk_size):
    if not hasattr(iterable, '__iter__'):
        # can't use "return" and "yield" in the same function
        yield iterable
    else:
        i = 0
        chunk = []
        for item in iterable:
            chunk.append(item)
            i += 1
            if not i % chunk_size:
                yield chunk
                chunk = []
        if chunk:
            # some items will remain which haven't been yielded yet,
            # unless len(iterable) is divisible by chunk_size
            yield chunk

# template
#    <table align="center" width="100%">
#        {% for chunk in images|chunks:3 %}
#            <tr>
#                {% for image in chunk %}
#                    <td align="center" valign="bottom">
#                        <img src="{{ image.thumb }}" alt="{{ image.name }}"/>
#                    </td>
#                {% endfor %}
#            </tr>
#            <tr> 
#                {% for image in chunk %}
#                    <td align="center">
#                        {{ image.name }}<br/>
#                        {{ image.description }}
#                    </td>
#                {% endfor %}
#            </tr>
#        {% endfor %}
#    </table>