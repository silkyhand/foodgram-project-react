from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import (Favorite, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Tag)


class IngredientInline(TabularInline):
    model = IngredientAmount
    min_num = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author',
                    'total_in_favorites', 'pk')
    list_filter = ('author', 'name', 'tags')
    empty_value_display = '-пусто-'
    inlines = (
        IngredientInline,
        )

    def total_in_favorites(self, obj):
        return obj.favorite.count()


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug', 'pk')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount', 'pk')
    search_fields = ('recipe',)
    list_filter = ('recipe',)
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'recipe',
    )
    search_fields = ('recipe',)
    list_filter = ('recipe',)
    empty_value_display = '-пусто-'


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'recipe',
    )
    search_fields = ('recipe',)
    list_filter = ('recipe',)
    empty_value_display = '-пусто-'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Tag, TagAdmin)
