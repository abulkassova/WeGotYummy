
from django import forms
from .models import User, Role, IngredientCategory, Ingredient, Recipe
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 
                  'age',
                  'email',
                  'phone',
                  'address',
                  'password1',
                  'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'input-control'
    }))
    age = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'input-control'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-control'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-control'
    }))

class CreateIngredientCategoryForm(forms.ModelForm):
    class Meta:
        model = IngredientCategory
        fields = ('name',)

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-control'
    }))

class CreateIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name',
                  'category',
                  'measurementUnit',
                  'calories_per_unit',
                  'fat_per_unit',
                  'carbohydrates_per_unit',
                  'protein_per_unit')
        
    category_choice = forms.ModelChoiceField(
        queryset=IngredientCategory.objects.all(),  # Provide a queryset of existing discounts
        required=False,  # Make it optional
        widget=forms.Select(attrs={'class': 'ingredient-category-select'}),
    )

class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title',
                 'cookingTime',
                 'servingSize',
                 'owner',
                 'difficulty',
                 'ingredients',
                 'posted'
                )
        
class CreateRoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ('name',)


class CreateRecipeIngredientForm(forms.Form):
    recipes = forms.ModelChoiceField(
        queryset=Recipe.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'info'}),
    )
    ingredients = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'info'}),
    )

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'input100'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your username',
        'class': 'input100'
    }))