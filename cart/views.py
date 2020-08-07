from django.shortcuts import render, redirect

# Show the cart page
def view_cart(request):

    return render(request, 'cart/cart.html')

# Add the the specified quantity of the selected game to the cart
def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
