from django import forms
from .models import UserAccount


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('default_first_name', 'default_last_name', 'default_phone_number',
                  'default_street_address1', 'default_street_address2',
                  'default_town_or_city', 'default_postcode',
                  'default_county', 'default_country')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County or Region',
        }

        # Apply placeholders
        for field in self.fields:
            if field != 'default_country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Remove the field labels
            self.fields[field].label = False

