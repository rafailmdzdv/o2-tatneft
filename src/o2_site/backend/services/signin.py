from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


def signin_user(request_data: dict):
    username = request_data.get('username')
    password = request_data.get('password')
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
