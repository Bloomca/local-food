from django import forms

class FoodSuggestionForm(forms.Form):
  title = forms.CharField(label="Title in english", max_length=200)
  original_name = forms.CharField(label="Title in original language (one of)", max_length=200)
  description = forms.CharField(label="Description", widget=forms.Textarea)
  image_url = forms.URLField(label="URL with an image", max_length=300)
  countries = forms.CharField(
    label="Countries where you can find it",
    help_text="Separate several countries by commas",
    max_length=200)
  email = forms.EmailField(
    label="Your email to notify you after we publish it",
    help_text="optional",
    max_length=254,
    required=False)