from rest_framework.serializers import ModelSerializer

from app import models


class FuelCardSerializer(ModelSerializer):

    class Meta:
        model = models.FuelCard
        fields = ['id', 'number', 'took_time', 'changed_time']
