from django import forms
from .models import UserAccount


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('default_phone_number',
                  'default_street_address1', 'default_street_address2',
                  'default_town_or_city', 'default_postcode',
                  'default_county',)
