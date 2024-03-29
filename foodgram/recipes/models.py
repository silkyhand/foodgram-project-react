from django.core.validators import MinValueValidator
from django.db import models

from users.models import CustomUser


class Ingredient(models.Model):
    """Модель ингредиентов"""
    name = models.CharField('Название ингредиента', max_length=255)
    measurement_unit = models.CharField('Eдиница измерения', max_length=50)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    """Модель соединения ингредиента и его количества с рецептом"""
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   verbose_name='Ингредиент')
    recipe = models.ForeignKey('Recipe',
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    amount = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(
                1, message='Минимальное количество ингредиента 1'),),
        verbose_name='Количество')

    def __str__(self):
        return self.ingredient.name

    class Meta:
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        constraints = [
            models.UniqueConstraint(fields=['ingredient', 'recipe'],
                                    name='unique ingredients recipe')
        ]


class Tag(models.Model):
    name = models.CharField('Тег', max_length=50, unique=True)
    color = models.CharField('Цвет', max_length=50)
    slug = models.CharField('slug', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    """Модель рецептов"""
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )
    name = models.CharField(
        'Называние',
        max_length=255
    )
    image = models.ImageField(
        'Картинка',
        upload_to='recipes/'
    )
    text = models.TextField(
        'описание рецепта',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientAmount',
        related_name='recipes',
        verbose_name='Ингредиент'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги'
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(
                1, message='Минимальное время приготовления 1'),),
        verbose_name='Время приготовления')

    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    """Модель любимых рецептов"""
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='fan',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique favorite_recipe_user')
        ]


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='buyer',
        verbose_name='Покупатель'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shoppinglist',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_user_shoppingcart')
        ]
