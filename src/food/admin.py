from django.contrib import admin

from .models import Country, Food, Origin, FoodSuggestion

# Register your models here.

admin.site.register(Country)
admin.site.register(Food)
admin.site.register(Origin)
admin.site.register(FoodSuggestion)
