from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app import models, serializers


class FuelCardViewSet(ModelViewSet):

    queryset = models.FuelCard.objects.all()
    serializer_class = serializers.FuelCardSerializer

    @action(detail=False,
            url_path=r'random')
    def get_random_number(self, _: Request) -> Response:
        filtered_numbers = models.FuelCard.objects.filter(is_took=False)
        random_number = filtered_numbers.order_by('?')[0]
        serializer = self.get_serializer(random_number)
        return Response(serializer.data)

    @action(detail=False,
            methods=['put'],
            url_path=r'send_card/(?P<number>\d*)')
    def send_card(self, _: Request, number: int = None):
        pass
