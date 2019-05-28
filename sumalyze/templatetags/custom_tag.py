from django import template

register = template.Library()

@register.filter(name='idx')
def get_at_index(object_list, index):
    return object_list[index]