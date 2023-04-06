from rest_framework.response import Response
from rest_framework.request import Request

from backend import forms


def signup_user(request: Request) -> Response:
    form = forms.RegistrationForm(data=request.data)
    if form.is_valid():
        form.save()
        return Response({"status": "success"})
    error = list(form.errors.values())
    return Response({"status": "failed", "error": error})
