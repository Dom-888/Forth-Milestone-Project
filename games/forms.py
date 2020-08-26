from django import forms
from .models import Game, Category, Included


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        
        # Apply display names to the category field
        display_names = []
        for category in categories:
	        display_names.append((category.id, category.display_name))

        self.fields['category'].choices = display_names


class IncludedForm(forms.ModelForm):

    class Meta:
        model = Included
        fields = ('item','quantity')

    #game = forms.ImageField() # The game must be the same of the new game primary key, somehow





