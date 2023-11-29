from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.db.models import Q
from WeGotYummy.middleware.stats_middleware import StatsMiddleware
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def imprint(request):
    return render(request, 'imprint.html')

def maintenance(request):
    if request.user.is_authenticated == False:
        return redirect('/')

    return render(request, 'maintenance.html')

def create_user(request):
    if request.user.is_authenticated == False:
        return redirect('/')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
        
            user.save()

            return redirect('/')
        else:
            StatsMiddleware.log_error(request, form.errors.as_text())
    else:
        form = RegistrationForm()

    return render(request, 'forms/user.html', {
        'form': form
    })

def create_ingredient_category(request):
    if request.user.is_authenticated == False:
        return redirect('/')

    if request.method == 'POST':
        form = CreateIngredientCategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
        
            category.save()

            return redirect('/')
        else:
            StatsMiddleware.log_error(request, form.errors.as_text())
    else:
        form = CreateIngredientCategoryForm()

    return render(request, 'forms/category.html', {
        'form': form
    })


def create_ingredient(request):
    if request.user.is_authenticated == False:
        return redirect('/')

    if request.method == 'POST':
        form = CreateIngredientForm(request.POST)

        if form.is_valid():
            ingredient = form.save(commit=False)
        
            ingredient.save()

            return redirect('/')
        else:
            StatsMiddleware.log_error(request, form.errors.as_text())
    else:
        form = CreateIngredientForm()

    return render(request, 'forms/ingredient.html', {
        'form': form
    })

def create_recipe(request):
    if request.user.is_authenticated == False:
        return redirect('/')

    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
        
            recipe.save()

            return redirect('/')
        else:
            StatsMiddleware.log_error(request, form.errors.as_text())
    else:
        form = CreateRecipeForm()

    return render(request, 'forms/recipe.html', {
        'form': form
    })

def create_role(request):
    if request.user.is_authenticated == False:
        return redirect('/')

    if request.method == 'POST':
        form = CreateRoleForm(request.POST)

        if form.is_valid():
            role = form.save(commit=False)
        
            role.save()

            return redirect('/')
        else:
            StatsMiddleware.log_error(request, form.errors.as_text())
    else:
        form = CreateRoleForm()

    return render(request, 'forms/role.html', {
        'form': form
    })

def create_recipe_ingredient(request):
    if request.user.is_authenticated == False:
        return redirect('/')

    if request.method == 'POST':
        form = CreateRecipeIngredientForm(request.POST)

        if form.is_valid():

            recipe = form.cleaned_data['recipes']

            ingredients = form.cleaned_data['ingredients']

            recipe.ingredients.add(ingredients)

            return redirect('/')
        else:
            StatsMiddleware.log_error(request, form.errors.as_text())
    else:
        form = CreateRecipeIngredientForm()

    return render(request, 'forms/recipe_ingredient.html', {
        'form': form
    })

def search_users(request):
    query = request.GET.get('query', '')
    role_id = request.GET.get('role', 0)
    roles = Role.objects.all()
    users = User.objects.all()
    
    if role_id:
        users = users.filter(role_id=role_id)

    if query:
        users = users.filter(Q(username__icontains=query) | Q(address__icontains=query))

    user_recipes_counts = [{'user': user, 'recipes_count': user.recipes.count()} for user in users]

    return render(request, 'search/search_users.html', {
        'user_recipes_counts': user_recipes_counts,
        'query': query,
        'roles': roles,
        'role_id': int(role_id)
    })

def users_detail(request, pk):

    user = get_object_or_404(User, pk=pk)

    return render(request, 'search/user_detail.html', {
        'user': user,
        'recipes': user.recipes.all()
    })


def search_recipes(request):

    query = request.GET.get('query', '')
    difficulty = request.GET.get('difficulty', '')

    difficulties = ['Undefined', 'Easy', 'Normal', 'Difficult']
    recipes = Recipe.objects.all()
    
    if difficulty:
        recipes = recipes.filter(difficulty=difficulty)

    if query:
        recipes = recipes.filter(Q(title__icontains=query))

    recipes_ingredients_counts = [{'recipe': recipe, 'ingredients_count': recipe.ingredients.count()} for recipe in recipes]

    return render(request, 'search/search_recipes.html', {
        'recipes_ingredients_counts': recipes_ingredients_counts,
        'query': query,
        'difficulties': difficulties,
        'chosen_difficulty': difficulty,
    })

def recipes_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    return render(request, 'search/recipe_detail.html', {
        'recipe': recipe,
        'ingredients': recipe.ingredients.all()
    })

def search_ingredients(request):

    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)

    categories = IngredientCategory.objects.all()
    ingredients = Ingredient.objects.all()
    
    if category_id:
        ingredients = ingredients.filter(category_id=category_id)

    if query:
        ingredients = ingredients.filter(Q(name__icontains=query))

    return render(request, 'search/search_ingredients.html', {
        'ingredients': ingredients, 
        'query': query,
        'categories': categories,
        'chosen_category': int(category_id),
    })

def ingredients_detail(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    return render(request, 'search/ingredient_detail.html', {
        'ingredient': ingredient,
    })

def autocomplete_users(request):
    query = request.GET.get('term', '')
    users = User.objects.filter(username__startswith=query).values_list('username', flat=True)
    usernames = list(users)
    return JsonResponse(usernames, safe=False)

def autocomplete_ingredients(request):
    query = request.GET.get('term', '')
    ingredients = Ingredient.objects.filter(name__startswith=str(query)).values_list('name', flat=True)
    names = list(ingredients)
    return JsonResponse(names, safe=False)

def autocomplete_recipes(request):
    query = request.GET.get('term', '')
    recipes = Recipe.objects.filter(title__startswith=query).values_list('title', flat=True)
    titles = list(recipes)
    return JsonResponse(titles, safe=False)