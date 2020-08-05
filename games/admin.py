from django.contrib import admin
from .models import Game, Category, Included

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )

class IncludedAdmin(admin.ModelAdmin):
    list_display = (
        'game',
        'quantity',
        'item'
    )

admin.site.register(Game, GameAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Included, IncludedAdmin)