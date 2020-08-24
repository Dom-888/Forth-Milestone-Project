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
    context = {
        'user_name': user,
        'orders': orders
    }

    return render(request, template, context)

# def order_history():