from django import forms
from user.models import Student


class StudentForms(forms.ModelForm):
    class Meta:
        model = Student

        fields = ['image']
