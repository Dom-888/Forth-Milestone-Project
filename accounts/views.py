from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserAccount
from .forms import UserAccountForm
from checkout.models import Order

# Show a form with user information and allows to update them
def account(request):
    user = get_object_or_404(UserAccount, user=request.user)
    form = UserAccountForm(request.POST, instance=user)
    template = 'accounts/delivery_information.html'

    # Update the user information
    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account updated!')

    context = {
        'user_name': user,
        'form': form
    }

    return render(request, template, context)


# Show the user order history
def order_history(request):
    user = get_object_or_404(UserAccount, user=request.user)
    orders = user.orders.all()
    template = 'accounts/order_history.html'

    context = {
        'user_name': user,
        'orders': orders, 
    }
    print("something")
    return render(request, template, context)
