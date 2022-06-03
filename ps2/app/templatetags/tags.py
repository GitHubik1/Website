from atexit import register
from django import template

register = template.Library()

@register.filter(name='edit')
def edit(value, arg):
    value = value + arg
    return ''