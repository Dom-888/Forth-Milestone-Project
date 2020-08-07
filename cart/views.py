from django.shortcuts import render

# Show the cart conents page
def view_cart(request):
    return render(request, 'cart/cart.html')