from django.shortcuts import render, redirect, reverse

# Show the cart page
def view_cart(request):

    return render(request, 'cart/cart.html')

# Add the specified quantity of the selected game to the cart
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

# Remove the item from the cart
def remove_cart_item(request, item_id):
    cart = request.session.get("cart", {})
    cart.pop(item_id)
    request.session["cart"] = cart
    # Message: "Item removed from cart"
    return redirect(reverse("view_cart"))

# Change item quantity in the cart
def update_cart_item_quantity(request, item_id):
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))