from django.contrib import admin
from .models import Game, Category, Included

# Register your models here.

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Included)