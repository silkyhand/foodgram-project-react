from django.db import models
from users.models import CustomUser


class Ingredient(models.Model):
    """Модель ингредиентов"""
    title = models.CharField('Название ингредиента', max_length=255)
    measurement_unit = models.CharField('единица измерения', max_length=50)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.title


class IngredientAmount(models.Model):
    """Модель соединения ингредиента и его количества с рецептом"""
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   related_name='amounts',
                                   verbose_name='Ингредиент')
    recipe = models.ForeignKey('Recipe',
                               on_delete=models.CASCADE,
                               related_name='ingredient_amounts',
                               verbose_name='Рецепт')
    amount = models.PositiveSmallIntegerField('Количество')

    def __str__(self):
        return self.ingredient.title


class Tag(models.Model):
    name = models.CharField('Тег', max_length=15, unique=True)
    color = models.CharField('Цвет', max_length=15)
    slug = models.CharField('slug', max_length=15, unique=True)

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
        verbose_name='Автор'
    )
    name = models.CharField(
        'Называние',
        max_length=255        
        )
    image = models.ImageField(
        'Картинка',
        upload_to='recipes/' 
    )
    description = models.TextField(
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
        verbose_name='Тег'
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления'
    )

    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name[:6]


class Favorite(models.Model):
    """Модель избранных"""
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='fan'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingList(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='buyer'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shoppinglist'
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'