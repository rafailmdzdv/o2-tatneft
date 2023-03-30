from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from app import models, serializers


class FuelCardViewSet(ModelViewSet):

    queryset = models.FuelCard.objects.all()
    serializer_class = serializers.FuelCardSerializer

    @action(detail=False,
            methods=['put'],
            url_path=r'send_card/(?P<number>\d*)')
    def send_card(self, _: Request, number: int = None):
        pass
