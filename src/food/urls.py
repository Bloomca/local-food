from django.urls import path

from .views import index, food, country, countries, food_list, about, lucky, search, categories, food_suggestion

urlpatterns = [
    path('', index),
    path('food/<food_slug>', food),
    path('country/<country_code>', country),
    path('food', food_list),
    path('countries', countries),
    path('about', about),
    path('lucky', lucky),
    path('search', search),
    path('categories', categories),
    path('suggestions/food', food_suggestion)
]