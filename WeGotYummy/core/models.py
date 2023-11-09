from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create your models here.
class User(AbstractUser):
    # user_name = models.CharField(max_length=50)
    # password_hash = models.TextChoices()

    # role can have many users
    role = models.ForeignKey(Role, related_name='users', on_delete=models.CASCADE, null=True)

    # first_name = models.CharField(max_length=127)
    # last_name = models.CharField(max_length=127)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    age=models.IntegerField(validators=[
            MinValueValidator(limit_value=0, message="Enter the valid age."),
            MaxValueValidator(limit_value=100, message="Enter the valid age.")
        ], default=0)
    # email = models.EmailField()

    def __str__(self) -> str:
        return self.username


class IngredientCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    category = models.ForeignKey(IngredientCategory, related_name='igredients', on_delete=models.CASCADE)

    #
    class MeasurmentUnits(models.TextChoices):
        PIECES = 'Pieces'
        GRAMS = 'Grams'
        KILOGRAMS = 'Kilograms'
        POUNDS = 'Pounds'
        MILLILITERS = 'Milliliters'
        LITERS = 'Liters'
        TEASPOONS = 'Teaspoons'
        TABLESPOONS = 'Tablespoons'
        CUPS = 'Cups'

    measurementUnit = models.CharField(choices=MeasurmentUnits.choices, default=MeasurmentUnits.PIECES, max_length=50)
    #

    calories_per_unit = models.FloatField()
    fat_per_unit = models.FloatField()
    carbohydrates_per_unit = models.FloatField()
    protein_per_unit = models.FloatField()

    def __str__(self) -> str:
        return self.name

class Recipe(models.Model):

    title = models.CharField(max_length=255)

    cookingTime = models.IntegerField()
    posted = models.BooleanField()
    servingSize = models.PositiveIntegerField()
    

    owner = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)


    class DifficultyType(models.TextChoices):
        UNDEFINED = ''
        EASY = 'Easy'
        NORMAL = 'Normal'
        DIFFICULT = 'Difficult'

    difficulty = models.CharField(choices=DifficultyType.choices, default=DifficultyType.UNDEFINED, max_length=50)

    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')

    def __str__(self) -> str:
        return self.title