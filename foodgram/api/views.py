import csv
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters

from api.filters import RecipeFilter
from recipes.models import (ShoppingCart, Favorite, Ingredient, IngredientAmount,
                            Recipe, Tag, ShoppingCart)
from api.pagination import ProjectPagination
from api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from api.serializers import (PartRecipeSerializer, IngredientSerializer,
                             RecipeSerializer, TagSerializer)


class TagsViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientsViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = ProjectPagination
    filter_class = RecipeFilter
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post', 'delete'],
            permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        user = request.user
        recipe = Recipe.objects.get(pk=pk)
        favorite_object = Favorite.objects.filter(user=user, recipe=recipe)
        if request.method == 'POST':
            if favorite_object.exists():
                return Response({
                    'errors': 'Вы уже подписаны на этот рецепт'
                }, status=status.HTTP_400_BAD_REQUEST)
            Favorite.objects.create(user=user, recipe=recipe)
            serializer = PartRecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if not favorite_object.exists():
            return Response({
                'errors': 'Вы не подписаны на этот рецепт'
            }, status=status.HTTP_400_BAD_REQUEST)
        favorite_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    @action(detail=True, methods=['post', 'delete'],
            permission_classes=[IsAuthenticated])
    def shopping_cart(self, request, pk=None):
        user = request.user
        recipe = Recipe.objects.get(pk=pk)
        recipe_in_cart = ShoppingCart.objects.filter(user=user, recipe=recipe)
        if request.method == 'POST':
            if recipe_in_cart.exists():
                return Response({
                    'errors': 'Рецепт уже есть в списке покупок'
                }, status=status.HTTP_400_BAD_REQUEST)
            ShoppingCart.objects.create(user=user, recipe=recipe) 
            serializer = PartRecipeSerializer(recipe) 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        if not recipe_in_cart.exists():
            return Response({
                'errors': 'Вы не подписаны на этот рецепт'
            }, status=status.HTTP_400_BAD_REQUEST)
        recipe_in_cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
                

    @action(detail=False, methods=['get'],
            permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        final_list = {}
        ingredients = IngredientAmount.objects.filter(
            recipe__shoppinglist__user=request.user).values_list(
            'ingredient__name', 'ingredient__measurement_unit',
            'amount')
        for item in ingredients:
            name = item[0]
            if name not in final_list:
                final_list[name] = {
                    'measurement_unit': item[1],
                    'amount': item[2]
                }
            else:
                final_list[name]['amount'] += item[2]
         
        response = HttpResponse(content_type='text/plain') 
        response['Content-Disposition'] = 'attachment; filename="shopping_cart.txt"' 
        writer = csv.writer(response) 
        for i, (name, data) in enumerate(final_list.items(), 1):
            writer.writerow([f'{i}) {name} - {data["amount"]},'
                                        f'{data["measurement_unit"]}']) 
        return response 
