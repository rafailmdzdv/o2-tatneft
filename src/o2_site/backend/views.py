from django.http.request import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from backend.services import (credentials,
                              logout,
                              signin,
                              signup)


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


@csrf_exempt
def signup_user(request: HttpRequest) -> Response | None:
    if request.method == 'POST':
        return signup.signup_user(request)
