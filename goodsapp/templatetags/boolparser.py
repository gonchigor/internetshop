from django import template

register = template.Library()


@register.filter
def boolparser(value):
    if value:
        return 'Есть на складе'
    return "Нет на складе"
