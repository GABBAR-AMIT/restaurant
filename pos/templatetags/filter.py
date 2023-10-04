from django import template

register = template.Library()

@register.filter
def calc_total(quantity, item_price):
    return quantity * item_price