import csv

from django.http import HttpResponse

from recipes.models import IngredientAmount


def make_shopping_cart(request):
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
    response['Content-Disposition'] = ('attachment; '
                                       'filename="shopping_cart.txt"')
    writer = csv.writer(response)
    for i, (name, data) in enumerate(final_list.items(), 1):
        writer.writerow([f'{i}) {name} - {data["amount"]},'
                         f'{data["measurement_unit"]}'])
    return response
