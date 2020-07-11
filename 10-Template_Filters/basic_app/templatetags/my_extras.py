# -*- coding: utf-8 -*-

from django import template

register = template.Library()


# register Template filters using Decorators
@register.filter(name = "cut")
def cut(value, arg):
    
    """
    This cuts all value of "arg" from string
    """
    
    return value.replace(arg, '')

#register.filter('cut', cut)

