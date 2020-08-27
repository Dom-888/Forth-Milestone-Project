from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from games.models import Game
from cart.contexts import cart_contents
import stripe

from accounts.models import UserAccount
from accounts.forms import UserAccountForm


def checkout(request):
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        # If the payment is successful
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
                    messages.error(request) 
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            
            messages.info(request, 'Payment successful! \r You will receive an email with the order details.')
            request.session["cart"] = {}

            if request.user.is_authenticated:
                account = UserAccount.objects.get(user=request.user)
                save_info = request.session.get('save_info')
                order.user_account = account
                order.save()

                # Save the user's info
                if save_info:
                    user_data = {
                        'default_first_name': order.first_name,
                        'default_last_name': order.last_name,
                        'default_phone_number': order.phone_number,
                        'default_country': order.country,
                        'default_postcode': order.postcode,
                        'default_town_or_city': order.town_or_city,
                        'default_street_address1': order.street_address1,
                        'default_street_address2': order.street_address2,
                        'default_county': order.county,
                    }
                    user_account_form = UserAccountForm(user_data, instance=account)
                    if user_account_form.is_valid():
                        user_account_form.save()

            return redirect(reverse("games")) # Should return to {% url 'order_history' %}
        
        # If the payment fails
        else:
            messages.info(request, 'Sorry, we were unable to process the payment.')                    

    else: # GET
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
        
        # Prefill the form with the user's information, if he is authenticated
        if request.user.is_authenticated:
            try:
                account = UserAccount.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'first_name': account.default_first_name,
                    'last_name': account.default_last_name,
                    'phone_number': account.default_phone_number,
                    'country': account.default_country,
                    'postcode': account.default_postcode,
                    'town_or_city': account.default_town_or_city,
                    'street_address1': account.default_street_address1,
                    'street_address2': account.default_street_address2,
                    'county': account.default_county,
                })
            except UserAccount.DoesNotExist:
                order_form = OrderForm()
        else:
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



