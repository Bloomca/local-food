from django.shortcuts import render
from django.db.models.aggregates import Count
from django.template import RequestContext
from django.http import HttpResponseRedirect
from random import randint
from django.shortcuts import redirect

from .models import Country, Food, Origin, FoodSuggestion
from .forms import FoodSuggestionForm

def index(request):
  countries = Country.objects.all()[:4]
  food_list = Food.objects.all()[:4]

  context = RequestContext(request, {
    'countries': countries, 'food_list': food_list
  })
  return render(request, 'food/index.html', context=context.flatten())

def search(request):
  if request.method == 'POST':
    request_query = request.POST.get('query', '')
    return HttpResponseRedirect('/food?q=' + request_query)

def countries(request):
  countries = Country.objects.all()

  context = {'countries': countries}
  return render(request, 'food/countries.html', context=context)

def food_list(request):
  search = request.GET.get('q', '')

  if search == '':
    food_list = Food.objects.all()

    context = {'food_list': food_list}
    return render(request, 'food/food_list.html', context=context)
  else:
    food_list_title = Food.objects.filter(title__contains=search)
    food_list_original_title = Food.objects.filter(original_name__contains=search)

    food_list = food_list_title.union(food_list_original_title).all()
    context = {'food_list': food_list, 'search': True, 'search': search}
    return render(request, 'food/food_list_search.html', context=context)

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

def categories(request):
  vegeterian = Food.objects.filter(vegeterian=True).exclude(vegan=True).all()
  vegan = Food.objects.filter(vegan=True).all()
  beverages = Food.objects.filter(beverage=True).all()
  context = {'vegeterian': vegeterian, 'vegan': vegan, 'beverages': beverages}
  return render(request, 'food/categories.html', context=context)

def food_suggestion(request):
  if request.method == "POST":
    form = FoodSuggestionForm(request.POST)

    if form.is_valid():
      pristine_form = FoodSuggestionForm()
      suggestion = FoodSuggestion(
        title=form.data['title'],
        original_name=form.data['original_name'],
        description=form.data['description'],
        email=form.data['email'],
        image_url=form.data['image_url'],
        countries=form.data['countries']
      )
      suggestion.save()
      context = {'form': pristine_form, 'success': True}
      return render(request, 'food/suggestion.html', context=context)
    else:
      context = {'form': form}
      return render(request, 'food/suggestion.html', context=context)

  form = FoodSuggestionForm()
  context = {'form': form}
  return render(request, 'food/suggestion.html', context=context)




