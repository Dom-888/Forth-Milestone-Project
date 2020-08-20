from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from games.models import Game
from cart.contexts import cart_contents
import stripe


def checkout(request):
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()

            # Iterate through the cart items to create the order_line_items
            for item_id, quantity in cart.items(): 
                try:
                    game = Game.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        game=game,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except:
                    messages.error(request) #This may require a second parameter
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.info(request, 'A problem was detected with the information entered, please try again.')                    

    else: # GET
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
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number ):
    print("please just work, please")
