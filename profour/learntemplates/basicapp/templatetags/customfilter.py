from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    # This cuts out all vals of arg from string
    return value.replace(arg,'')

#register.filter('cut',cut)