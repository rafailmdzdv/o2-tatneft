from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from backend.services.map import get_gs_map


class MapViewSet(ViewSet):

    def list(self, _: Request):
        html_map = get_gs_map()
        return Response({'map': html_map})
