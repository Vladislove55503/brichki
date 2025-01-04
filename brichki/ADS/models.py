from contextlib import nullcontext

from django.db import models

from brichki.FILTER.models import Brand
from brichki.FILTER.models import Model
from brichki.FILTER.models import Generation


class Ads(models.Model):

    class Body(models.IntegerChoices):
        SUV = 0, 'Внедорожник'
        SEDAN = 1, 'Седан'
        HATCHBACK = 2, 'Хэтчбек'
        LIFTBACK = 3, 'Лифтбек'
        STATION_WAGON = 4, 'Универсал'
        MINIVAN_SERVICE = 5, 'Минивэн'
        COUPE = 6, 'Купе'
        PICKUP_TRUCK = 7, 'Пикап'
        CABRIOLET = 8, 'Кабриолет'
        VAN = 9, 'Фургон'

    body = models.IntegerField(choices=Body.choices)
    # engine =
    # engine_capacity = models.FloatField()
    # drive =
    # broken =
    # mileage = models.IntegerField(default=0)

    # price = models.IntegerField(null=True, blank=True)
    # comment = models.CharField(max_length=10000) #default=''

    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey('Model', on_delete=models.SET_NULL, null=True)
    generation = models.ForeignKey('Generation', on_delete=models.SET_NULL, null=True)
