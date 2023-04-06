from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        # fields = ('username', 'password', 'email', 'first_name', 'middle_name', 'last_name', 'department')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # fields = ('username', 'password', 'email', 'first_name', 'middle_name', 'last_name', 'department')