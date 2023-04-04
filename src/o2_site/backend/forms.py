import json

from django import forms
from django.contrib.auth.hashers import make_password, check_password

from backend import models


class RegistrationForm(forms.Form):

    username = forms.CharField(max_length=40, error_messages={
        'required': 'Логин обязателен',
        'max_length': 'Длина логина превышает 40 символов'
    })
    email = forms.EmailField(error_messages={
        'required': 'Почта обязательна',
        'invalid': 'Введите действительный адрес электронной почты'
    })
    password = forms.CharField(error_messages={'required': 'Пароль необходим'})

    def save(self):
        user = models.User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        return user
