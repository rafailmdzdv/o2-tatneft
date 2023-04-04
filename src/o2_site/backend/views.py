import json

from django.contrib.auth import authenticate
from django.http.request import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from backend import error_messages, forms, models


class LoginView(APIView):

    def post(self, request: Request) -> Response:
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh_token = RefreshToken.for_user(user)
            data = {
                'success': True,
                'access_token': str(refresh_token.access_token),
                'refresh_token': str(refresh_token)
            }
            return Response(data)
        return Response({'success': False,
                         'error': 'Логин или пароль неверный'})


class LogoutView(APIView):

    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        refresh_token = RefreshToken(request.data['refresh_token'])
        refresh_token.blacklist()
        return Response({'success': True})


class ChangeUsernameView(APIView):

    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        form = forms.UpdateCredentialsForm(data=json.loads(request.body),
                                           instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            user.save()
            return Response({'success': True})
        else:
            error = list(form.errors.values())[0][0]
            return Response({'success': False,
                             'error': error})


class ChangeEmailView(APIView):

    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        form = forms.UpdateCredentialsForm(data=json.loads(request.body),
                                           instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            return Response({'success': True})
        else:
            error = list(form.errors.values())[0][0]
            return Response({'success': False,
                             'error': error})


@csrf_exempt
def register_user(request: HttpRequest) -> Response | None:
    if request.method == 'POST':
        form = forms.RegistrationForm(data=json.loads(request.body))
        if form.is_valid():
            form.save()
            return Response({"status": "success"})
        return Response({"status": "failed", "error": form.errors})
