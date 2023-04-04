import json

from rest_framework import response, request

from backend import forms


def signup_user(request: request.Request) -> response.Response:
    form = forms.RegistrationForm(data=json.loads(request.body))
    if form.is_valid():
        form.save()
        return response.Response({"status": "success"})
    error = list(form.errors.values())[0][0]
    return response.Response({"status": "failed", "error": error})
