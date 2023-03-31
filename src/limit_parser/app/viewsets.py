from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app import models, serializers
from app.services.pw import start_adding_limit_and_update_data
from app.services.random_number import get_random_card_and_update_data


class FuelCardViewSet(ModelViewSet):

    queryset = models.FuelCard.objects.all()
    serializer_class = serializers.FuelCardSerializer

    @action(detail=False,
            url_path=r'random')
    def get_random_number(self, _: Request) -> Response:
        serializer_data = get_random_card_and_update_data(self)
        return Response(serializer_data)

    @action(detail=False,
            methods=['put'],
            url_path=r'send_card/(?P<number>\d*)')
    def send_card(self, _: Request, number: str):
        start_adding_limit_and_update_data(number)
        return Response({'status': f'{number} successfull'})
