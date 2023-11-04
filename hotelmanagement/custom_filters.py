from django import template

register = template.Library()

@register.filter
def float_range(value):
    return range(int(value * 4))