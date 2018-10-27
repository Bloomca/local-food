from django.urls import path

from .views import index, food, country

urlpatterns = [
    path('', index),
    path('food/<food_slug>', food),
    path('country/<country_code>', country)
]