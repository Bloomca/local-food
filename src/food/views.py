from django.shortcuts import render

from .models import Country

def index(request):
  countries = Country.objects.all()

  context = {'countries': countries}
  return render(request, 'food/index.html', context=context)

# def food(request, food_id):


