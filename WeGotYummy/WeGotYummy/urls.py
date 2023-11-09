"""
URL configuration for WeGotYummy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index_page'),
    path('index/', index, name='index_page'),
    path('imprint/', imprint, name='imprint_page'),
    path('maintenance/', maintenance, name='maintenance_page'),
    path('register/', create_user, name='register_page'),
    path('create-category/', create_ingredient_category, name="create-ingredient-category_page"),
    path('create-ingredient/', create_ingredient, name="create-ingredient_page"),
    path('create-recipe/', create_recipe, name='create-recipe_page'),
    path('create-role/', create_role, name='create-role_page'),
    path('create-recipe-ingedient/', create_recipe_ingredient, name='create-recipe-ingredient_page'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
