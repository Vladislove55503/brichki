import os
from uuid import uuid4

from django.db import models

from FILTER.models import (
    Brand,
    Model,
    Generation,
    Body,
    EngineType,
    BoostType,
    Drive,
    Broken,
)


class Ads(models.Model):
    brand = models.ForeignKey(Brand,
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='Марка',
                              )
    model = models.ForeignKey(Model,
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='Модель',
                              )
    generation = models.ForeignKey(Generation,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   verbose_name='Поколение',
                                   )
    body = models.ForeignKey(Body,
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name='Кузов',
                             )
    engine_type = models.ForeignKey(EngineType,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    verbose_name='Двигатель',
                                    )
    boost_type = models.ForeignKey(BoostType,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   verbose_name='Наддув',
                                   )
    drive = models.ForeignKey(Drive,
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='Привод',
                              )
    broken = models.ForeignKey(Broken,
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name='Битая',
                               )
    comment = models.ForeignKey('Comments',
                                on_delete=models.SET_NULL,
                                null=True,
                                verbose_name='Комментарий',
                                )
    engine_capacity = models.FloatField(verbose_name='Объём двигателя')
    mileage = models.IntegerField(default=0, verbose_name='Пробег')
    price = models.IntegerField(verbose_name='Цена')


    def __str__(self):
        return self.brand, self.generation, self.price


class Comments(models.Model):
    text = models.CharField(max_length=10000, blank=True, default='')

    def __str__(self):
        return self.text


def path_and_rename(instance, filename):
    upload_to = 'ADS/photos'
    ext = filename.split('.')[-1]
    filename = f'{uuid4().hex}.{ext}'

    return os.path.join(upload_to, filename)


class Photos(models.Model):
    ad = models.ForeignKey('Ads', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return f'Для объявления - {self.ad}'