from django.db import models
from django.db.models import SET_NULL

from FILTER.models import Brand
from FILTER.models import Model
from FILTER.models import Generation

class Parameters(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Body(Parameters, models.Model):
    pass


# class Body(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     value = models.IntegerField(unique=True)
#
#     def __str__(self):
#         return self.name

class EngineType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class BoostType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Drive(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Broken(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Ads(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name='Марка')
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, verbose_name='Модель')
    generation = models.ForeignKey(Generation, on_delete=models.SET_NULL, null=True, verbose_name='Поколение')

    body = models.ForeignKey('Body', on_delete=SET_NULL, null=True, verbose_name='Кузов')

    engine_type = models.ForeignKey('EngineType', on_delete=SET_NULL, null=True, verbose_name='Двигатель')
    boost_type = models.ForeignKey('BoostType', on_delete=SET_NULL, null=True, verbose_name='Наддув')
    engine_capacity = models.FloatField(verbose_name='Объём двигателя')

    drive = models.ForeignKey('Drive', on_delete=SET_NULL, null=True, verbose_name='Привод')
    broken = models.ForeignKey('Broken', on_delete=SET_NULL, null=True, verbose_name='Битая')

    mileage = models.IntegerField(default=0, verbose_name='Пробег')
    price = models.IntegerField(verbose_name='Цена')
    comment = models.CharField(max_length=10000, blank=True, default='', verbose_name='Комментарий')


    def __str__(self):
        return f'{self.brand}, {self.model}, {self.generation}, {self.engine_capacity}, {self.price}'