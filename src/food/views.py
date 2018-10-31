from django.shortcuts import render
from django.db.models.aggregates import Count
from random import randint
from django.shortcuts import redirect

from .models import Country, Food, Origin

def index(request):
  countries = Country.objects.all()[:4]
  food_list = Food.objects.all()[:4]

  context = {'countries': countries, 'food_list': food_list}
  return render(request, 'food/index.html', context=context)

def countries(request):
  countries = Country.objects.all()

  context = {'countries': countries}
  return render(request, 'food/countries.html', context=context)

def food_list(request):
  food_list = Food.objects.all()

  context = {'food_list': food_list}
  return render(request, 'food/food_list.html', context=context)

def food(request, food_slug):
  food = Food.objects.get(slug=food_slug)
  countries_list = []

  countries = food.country_set.all()
  for country in countries:
    origin = Origin.objects.get(food=food, country=country)
    countries_list.append((country, origin))

  context = {'food': food, 'countries_list': countries_list}
  return render(request, 'food/food.html', context=context)

def country(request, country_code):
  country = Country.objects.get(code=country_code)

  print(country.foods.all())

  context = {'country': country}
  return render(request, 'food/country.html', context=context)

def about(request):
  return render(request, 'food/about.html')

def lucky(request):
  count = Food.objects.count()
  random_index = randint(0, count - 1)
  selected_food = Food.objects.all()[random_index]

  return redirect("/food/" + selected_food.slug)




