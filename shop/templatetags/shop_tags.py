from django import template

from shop.models import *


register = template.Library()

@register.simple_tag()
def get_contact():
    return Contact.objects.all()

@register.simple_tag()
def get_category():
    return Category.objects.all()
