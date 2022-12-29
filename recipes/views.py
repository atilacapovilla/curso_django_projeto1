from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

def home(request):
    # pegando dados aleatórios para teste
    # return render(request, 'recipes/pages/home.html', context={
    #     'recipes': [make_recipe() for _ in range(10)],
    # })

    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

    
def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

