from django.forms import ModelForm
from .models import Reviews
from django import forms

class ReviewForm(forms.Form):
    model = Reviews
    fields = ['review', 'reviewer', 'rating']

    widgets = {
        'rating': forms.CheckboxSelectMultiple(),
    }