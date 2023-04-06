from django.db import models


class FuelCard(models.Model):

    number = models.CharField(max_length=16)
    is_took = models.BooleanField()
    has_limit = models.BooleanField()
    took_time = models.DateTimeField(blank=True, null=True)
    changed_time = models.DateTimeField(blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
