from django import template

register = template.Libary()

@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg,'')

#register.filter('cut',cut)
