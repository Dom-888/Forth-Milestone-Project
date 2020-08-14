from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from games.models import Game

# Show the cart page
def view_cart(request):

    return render(request, 'cart/cart.html')

# Add the specified quantity of the selected game to the cart
def add_to_cart(request, item_id):

    game = get_object_or_404(Game, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'{game.name} added to cart') # Toast message
    else:
        cart[item_id] = quantity
        messages.success(request, f'{game.name} added to cart') # Toast message

    request.session['cart'] = cart
    return redirect(redirect_url)

# Remove the item from the cart
def remove_cart_item(request, item_id):
    game = get_object_or_404(Game, pk=item_id)
    cart = request.session.get("cart", {})
    cart.pop(item_id)
    messages.success(request, f'{game.name} removed from cart') # Toast message

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))

# Change item quantity in the cart
def update_cart_item_quantity(request, item_id):

    try:
        game = get_object_or_404(Game, pk=item_id)
        quantity = int(request.POST.get("quantity"))
        cart = request.session.get("cart", {})

        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Quantity for {game.name} updated') # Toast message
        else:
            cart.pop(item_id)
            messages.success(request, f'{game.name} removed from cart') # Toast message

        request.session["cart"] = cart
        return redirect(reverse("view_cart"))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)