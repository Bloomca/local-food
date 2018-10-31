from django.urls import path

from .views import index, food, country, countries, food_list

urlpatterns = [
    path('', index),
    path('food/<food_slug>', food),
    path('country/<country_code>', country),
    path('food', food_list),
    path('countries', countries)
]