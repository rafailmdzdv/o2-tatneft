import json

from django.forms import ModelForm
from rest_framework import response, request

from backend import forms


def change_user_credential(request: request.Request, credential: str):
    form = forms.UpdateCredentialsForm(data=json.loads(request.body),
                                       instance=request.user)
    if form.is_valid():
        _update_user_credential(form, credential)
        return response.Response({'success': True})
    else:
        error = list(form.errors.values())[0][0]
        return response.Response({'success': False,
                                  'error': error})


def _update_user_credential(form: ModelForm, credential: str) -> None:
    user = form.save(commit=False)
    if credential == 'username':
        user.username = form.cleaned_data[credential]
    if credential == 'email':
        user.email = form.cleaned_data[credential]
    user.save()
