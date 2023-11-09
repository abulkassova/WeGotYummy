from django.shortcuts import render, redirect
from .forms import *
from .models import Role

def index(request):
    return render(request, 'index.html')

def imprint(request):
    return render(request, 'imprint.html')

def maintenance(request):
    return render(request, 'maintenance.html')

def create_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
        
            user.save()

            return redirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'forms/user.html', {
        'form': form
    })

def create_ingredient_category(request):
    if request.method == 'POST':
        form = CreateIngredientCategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
        
            category.save()

            return redirect('/')
    else:
        form = CreateIngredientCategoryForm()

    return render(request, 'forms/category.html', {
        'form': form
    })


def create_ingredient(request):
    if request.method == 'POST':
        form = CreateIngredientForm(request.POST)

        if form.is_valid():
            ingredient = form.save(commit=False)
        
            ingredient.save()

            return redirect('/')
    else:
        form = CreateIngredientForm()

    return render(request, 'forms/ingredient.html', {
        'form': form
    })

def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
        
            recipe.save()

            return redirect('/')
    else:
        form = CreateRecipeForm()

    return render(request, 'forms/recipe.html', {
        'form': form
    })

def create_role(request):
    if request.method == 'POST':
        form = CreateRoleForm(request.POST)

        if form.is_valid():
            role = form.save(commit=False)
        
            role.save()

            return redirect('/')
    else:
        form = CreateRoleForm()

    return render(request, 'forms/role.html', {
        'form': form
    })

def create_recipe_ingredient(request):
    if request.method == 'POST':
        form = CreateRecipeIngredientForm(request.POST)

        if form.is_valid():

            recipe = form.cleaned_data['recipes']

            ingredients = form.cleaned_data['ingredients']

            recipe.ingredients.add(ingredients)

            return redirect('/')
    else:
        form = CreateRecipeIngredientForm()

    return render(request, 'forms/recipe_ingredient.html', {
        'form': form
    })