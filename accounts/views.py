from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserAccount

from checkout.models import Order


def account(request):
    user_name = get_object_or_404(UserAccount, user=request.user)

    template = 'accounts/personal_informations.html'
    context = {
        'user_name': user_name,
    }

    return render(request, template, context)

# def order_history():