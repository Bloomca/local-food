from django.shortcuts import render

from .models import Country, Food, Origin

def index(request):
  countries = Country.objects.all()

  context = {'countries': countries}
  return render(request, 'food/index.html', context=context)

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



