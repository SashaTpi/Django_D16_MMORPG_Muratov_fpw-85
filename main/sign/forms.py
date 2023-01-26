from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)
        widgets = {'username': TextInput(attrs={'size': 50, 'placeholder': 'Введите логин', 'title': 'Your name'}),
                   'first_name': TextInput(attrs={'size': 50, 'placeholder': 'Введите имя'}),
                   'last_name': TextInput(attrs={'size': 50, 'placeholder': 'Введите фамилию'}),
                   'email': TextInput(attrs={'size': 50, 'placeholder': 'Введите почту'}),
                   'password1': PasswordInput(attrs={'size': 50, 'placeholder': 'Введите пароль'}),
                   'password2': PasswordInput(attrs={'size': 50, 'placeholder': 'Введите почту'})}


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)