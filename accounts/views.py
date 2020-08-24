from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserAccount
from .forms import UserAccountForm
from checkout.models import Order


def account(request):
    user = get_object_or_404(UserAccount, user=request.user)
    form = UserAccountForm(request.POST, instance=user)
    orders = user.orders.all()
    template = 'accounts/delivery_information.html'

    # Update the user information
    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account updated!')

    context = {
        'user_name': user,
        'orders': orders, # Move orders in another view
        'form': form
    }

    return render(request, template, context)

# def order_history():