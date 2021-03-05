from django import forms

from session.models import Session


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session

        fields = ['title', 'description', 'video', 'time', 'status']
