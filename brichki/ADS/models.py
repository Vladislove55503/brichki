from django.db import models

from FILTER.models import Brand
from FILTER.models import Model
from FILTER.models import Generation

from FILTER.models import Body
from FILTER.models import EngineType
from FILTER.models import BoostType
from FILTER.models import Drive
from FILTER.models import Broken


class Ads(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name='Марка')
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, verbose_name='Модель')
    generation = models.ForeignKey(Generation, on_delete=models.SET_NULL, null=True, verbose_name='Поколение')

    body = models.ForeignKey(Body, on_delete=models.SET_NULL, null=True, verbose_name='Кузов')

    engine_type = models.ForeignKey(EngineType, on_delete=models.SET_NULL, null=True, verbose_name='Двигатель')
    boost_type = models.ForeignKey(BoostType, on_delete=models.SET_NULL, null=True, verbose_name='Наддув')

    engine_capacity = models.FloatField(verbose_name='Объём двигателя')
    drive = models.ForeignKey(Drive, on_delete=models.SET_NULL, null=True, verbose_name='Привод')
    broken = models.ForeignKey(Broken, on_delete=models.SET_NULL, null=True, verbose_name='Битая')
    mileage = models.IntegerField(default=0, verbose_name='Пробег')
    price = models.IntegerField(verbose_name='Цена')
    comment = models.CharField(max_length=10000, blank=True, default='', verbose_name='Комментарий')


    def __str__(self):
        return f'{self.brand}, {self.model}, {self.generation}, {self.engine_capacity}, {self.price}'