from django.shortcuts import render
from django.contrib import messages

from checkout.models import Order

def account(request):
    template = 'accounts/personal_informations.html'
    
    return render(template)


# def order_history():