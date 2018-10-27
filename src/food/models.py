from django.db import models

# Create your models here.

class Food(models.Model):
  title = models.CharField(max_length=200)
  original_name = models.CharField(max_length=200)
  slug = models.CharField(max_length=64, db_index=True, default="")
  description = models.TextField()
  vegeterian = models.BooleanField()
  vegan = models.BooleanField()
  pastry = models.BooleanField(default=False)
  beverage = models.BooleanField(default=False)
  alcoholic = models.BooleanField(default=False)

  def __str__(self):
    return self.title + '/' + self.original_name

class Country(models.Model):
  code = models.CharField(max_length=2)
  name = models.CharField(max_length=200)
  foods = models.ManyToManyField(Food, through='Origin')

  def __str__(self):
    return self.name

  class Meta:
    db_table = 'countries'

class Origin(models.Model):
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  description = models.TextField()

  def __str__(self):
    return str(self.food) + ' in ' + str(self.country)
