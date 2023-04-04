from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    username = models.CharField('Логин', max_length=40,
                                unique=True)
    email = models.EmailField('Почта', unique=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Region(models.Model):
    name = models.CharField(max_length=40)


class GasStation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    issuer_number = models.IntegerField(null=True)
    gs_number = models.IntegerField()
    companion_service_objects = models.TextField(null=True)
    additional_services = models.TextField(null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class FuelPrices(models.Model):
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE)
    ai92_taneko = models.FloatField(null=True)
    ai92 = models.FloatField(null=True)
    ai95_taneko = models.FloatField(null=True)
    ai95 = models.FloatField(null=True)
    dt = models.FloatField(null=True)
    dt_taneko = models.FloatField(null=True)
    ai98_taneko = models.FloatField(null=True)
    sug = models.FloatField(null=True)
    ai98 = models.FloatField(null=True)
    electro = models.FloatField(null=True)
    ai100 = models.FloatField(null=True)
    ad_blue = models.FloatField(null=True)
    ai80 = models.FloatField(null=True)
    dt_winter = models.FloatField(null=True)
    kpg = models.FloatField(null=True)
    dt_arctica = models.FloatField(null=True)
