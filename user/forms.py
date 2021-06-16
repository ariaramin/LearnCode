from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from user.models import Account


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account

        fields = ['image']


