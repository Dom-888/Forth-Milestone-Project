from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserAccount
from .forms import UserAccountForm
from checkout.models import Order


def account(request):
    user_name = get_object_or_404(UserAccount, user=request.user) # Do I need this?
    form = UserAccountForm(instance=account)
    orders = account.orders.all()
    template = 'accounts/personal_informations.html'
    context = {
        'user_name': user_name,
        'orders': orders
    }

    return render(request, template, context)

# def order_history():