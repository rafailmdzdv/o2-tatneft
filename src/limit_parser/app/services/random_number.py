from datetime import datetime

from rest_framework.viewsets import ModelViewSet

from app import models


def get_random_card_and_update_data(viewset: ModelViewSet) -> dict:
    serializer_data, random_card = _get_random_card(viewset)
    _update_card_data(random_card)
    return serializer_data


def _get_random_card(viewset: ModelViewSet) -> tuple[dict, models.FuelCard]:
    filtered_numbers = models.FuelCard.objects.filter(is_took=False)
    random_card = filtered_numbers.order_by('?')[0]
    return viewset.get_serializer(random_card).data, random_card


def _update_card_data(card: models.FuelCard) -> None:
    card.is_took = True
    card.took_time = datetime.now()
    card.save()
