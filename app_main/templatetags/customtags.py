from django import template
register = template.Library()
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_sub_cat_keys(item):
    return [ atoi(c) for c in re.split(r'(\d+)', item.subcategory if item.subcategory else '') ]

@register.filter
def splitVal(value,key):
    if value:
        value = value.split(key)
        return [x.strip(' ') for x in value[:6] if x]
    else:
        return value

@register.filter()
def humanize(value):
    if value:
        value = value.replace('_', ' ')
        return value.title()
    else:
        return value

@register.filter()
def sortSubCatQs(qs):
    print(sorted(qs,key=natural_sub_cat_keys))
    return sorted(qs,key=natural_sub_cat_keys)