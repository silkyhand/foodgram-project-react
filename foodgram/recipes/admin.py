from django.contrib import admin

<<<<<<< HEAD
from .models import (
     Favorite, Ingredient, IngredientAmount, Recipe, ShoppingCart, Tag
)
=======
from .models import (Favorite, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Tag)
>>>>>>> b9493539e8d201f268bbb533b81b2229f09eb75c


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'total_in_favorites')
    list_filter = ('author', 'name', 'tags')
    empty_value_display = '-пусто-'

    def total_in_favorites(self, obj):
        return obj.favorite.count()


class IngredientAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('name', 'measurement_unit')    
=======
    list_display = ('name', 'measurement_unit')
>>>>>>> b9493539e8d201f268bbb533b81b2229f09eb75c
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
