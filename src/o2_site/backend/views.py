import pathlib
from urllib.parse import urljoin, urlencode

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from backend import forms
from backend.services import (credentials,
                              logout,
                              responses,
                              signin,
                              signup)
from o2_site.settings import FRONTEND_HOST


class SigninView(APIView):

    def post(self, request: Request) -> Response:
        return signin.signin_user(request.data)


class LogoutView(APIView):

    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        return logout.logout_and_remove_token(request.data)


class ChangeUsernameView(APIView):

    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        return credentials.change_user_credential(request, 'username')


class ChangeEmailView(APIView):

    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        return credentials.change_user_credential(request, 'email')


class ChangePasswordView(APIView):

    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        user = request.user
        data = request.data
        form = forms.PasswordChangeForm(user, data)
        if form.is_valid():
            email = user.email
            token = default_token_generator.make_token(user)
            encoded_password = urlsafe_base64_encode(data['password'].encode())
            params = urlencode({'pass': encoded_password, 'token': token})
            reset_url = urljoin(FRONTEND_HOST,
                                f'changePasswordConfirm?{params}')
            message = f'Для смены пароля перейдите по ссылке {reset_url}'
            send_mail('Смена пароля', message, from_email=None,
                      recipient_list=[email])
            return Response({'success': True})
        else:
            return Response({'success': False, 'error': form.errors})


class ChangePasswordConfirmView(APIView):

    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        user = request.user
        data = request.data
        password = data['password']
        data['password'] = force_str(urlsafe_base64_decode(password))
        form = forms.PasswordChangeForm(user, data)
        form.is_valid()
        if default_token_generator.check_token(user, data['token']):
            form.save()
            return Response({'success': True})
        else:
            return Response({'success': False,
                             'message': 'Ссылка недействительна'})


class AzsListView(APIView):

    authentication_classes = [JWTAuthentication]

    def get(self, _: Request) -> HttpResponse:
        return responses.get_azs_file_response()


class NumberSenderReportView(APIView):

    authentication_classes = [JWTAuthentication]

    def get(self, _: Request) -> HttpResponse:
        return responses.get_ns_file_report_response()


class LimitParserReportView(APIView):

    authentication_classes = [JWTAuthentication]

    def get(self, _: Request) -> HttpResponse:
        return responses.get_lp_file_report_response()


@csrf_exempt
def signup_user(request: HttpRequest) -> Response | None:
    if request.method == 'POST':
        return signup.signup_user(request)
