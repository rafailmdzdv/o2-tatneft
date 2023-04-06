from urllib.parse import urlencode, urljoin

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.response import Response
from rest_framework.request import Request

from backend import forms, models
from o2_site import settings


def get_password_reset_response(request: Request) -> Response:
    form = _get_form(request)
    user = request.user
    data = request.data
    if form.is_valid():
        _send_mail(user, data)
        return Response({'success': True})
    else:
        return Response({'success': False, 'error': form.errors})


def get_confirm_password_reset_response(request) -> Response:
    form = _get_form(request)
    data = request.data
    password = data['password']
    data['password'] = force_str(urlsafe_base64_decode(password))
    form.is_valid()
    if default_token_generator.check_token(request.user, data['token']):
        form.save()
        return Response({'success': True})
    else:
        return Response({'success': False,
                         'message': 'Ссылка недействительна'})


def _get_form(request: Request) -> forms.PasswordChangeForm:
    return forms.PasswordChangeForm(request.user, request.data)


def _send_mail(user: models.User, data: dict) -> None:
    email = user.email
    token = default_token_generator.make_token(user)
    encoded_password = urlsafe_base64_encode(data['password'].encode())
    params = urlencode({'pass': encoded_password, 'token': token})
    reset_url = urljoin(settings.FRONTEND_HOST,
                        f'changePasswordConfirm?{params}')
    message = f'Для смены пароля перейдите по ссылке {reset_url}'
    send_mail('Смена пароля', message, from_email=None,
              recipient_list=[email])
