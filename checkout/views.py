from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.contexts import cart_contents
import stripe


def checkout(request):
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
	
	# Show a message and redirect the user if he try to access the checkout page with an empty cart
    cart = request.session.get('cart', {})
    if not cart:
        messages.info(request, "Your cart is empty")
        return redirect(reverse('games'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    # Stripe payment intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    
    order_form = OrderForm()

    if not stripe_publishable_key:
        messages.info(request, 'Stripe public key is missing.')
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_publishable_key': stripe_publishable_key,
    }

    return render(request, template, context)