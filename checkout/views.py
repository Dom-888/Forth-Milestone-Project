from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
import stripe


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.info(request, "Your cart is empty")
        return redirect(reverse('games'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H8WksByJBUTWj1SEhfAg9IPNhoFY2Btz00bU5k9cWrn2f3Ur3TtK9BvF90Za5DVV6ZhZtGtNBnunOmAE8vO1SaC00eKdWq2i3',
    }

    return render(request, template, context)