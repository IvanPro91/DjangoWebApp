from django import template

register = template.Library()

@register.filter()
def media_filter(path):
    print(path)
    if path:
        return f'/media/{path}'
    return '#'