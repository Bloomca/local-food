from django.urls import path

from .views import index, food

urlpatterns = [
    path('', index),
    path('food/<food_slug>', food)
]