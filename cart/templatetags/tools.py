from django import template

register = template.Library()

# Calculate the subtotals in the cart page
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity