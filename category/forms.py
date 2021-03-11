from django import forms
from .models import Category


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category

        fields = [
            'title',
            'description',
            'image',
        ]
