from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


def logout_and_remove_token(request_data: dict) -> Response:
    refresh_token = RefreshToken(request_data['refresh_token'])
    refresh_token.blacklist()
    return Response({'success': True})
