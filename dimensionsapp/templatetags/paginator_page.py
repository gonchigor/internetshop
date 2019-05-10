from django import template

register = template.Library()


@register.filter
def paginator_page(value, arg):
    qd = value.copy()
    qd['page'] = arg
    return '?' + qd.urlencode()
