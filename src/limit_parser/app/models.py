from django.db import models


class FuelCard(models.Model):

    number = models.CharField(max_length=16)
    is_took = models.BooleanField(default=False)
    has_limit = models.BooleanField(default=False)
    took_time = models.TimeField(blank=True, null=True)
    changed_time = models.TimeField(blank=True, null=True)
