from rest_framework.serializers import ModelSerializer

from app import models


class FuelCardSerializer(ModelSerializer):

    class Meta:
        model = models.FuelCard
        fields = ['id', 'number', 'is_took', 'has_limit',
                  'took_time', 'changed_time', 'limit']
