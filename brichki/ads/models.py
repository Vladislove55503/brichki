from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4


class Ad(models.Model):
    brand = models.ForeignKey('Brand',
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='Марка',
                              )
    model = models.ForeignKey('Model',
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='Модель',
                              )
    generation = models.ForeignKey('Generation',
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   verbose_name='Поколение',
                                   )
    body = models.ForeignKey('Body',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name='Кузов',
                             )
    engine_type = models.ForeignKey('EngineType',
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    verbose_name='Двигатель',
                                    )
    boost_type = models.ForeignKey('BoostType',
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   verbose_name='Наддув',
                                   )
    drive = models.ForeignKey('Drive',
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='Привод',
                              )
    broken = models.ForeignKey('Broken',
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name='Битая',
                               )
    comment = models.TextField(
        max_length=10000, blank=True, default='', verbose_name='Комментарий'
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, verbose_name='Автор'
        )
    engine_capacity = models.FloatField(verbose_name='Объём двигателя')
    mileage = models.IntegerField(default=0, verbose_name='Пробег')
    price = models.IntegerField(verbose_name='Цена')

    def get_absolute_url(self):
        from django.urls import reverse
        
        return reverse('ads:ad', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.brand}, {self.generation}, {self.price}, {self.author}'


def path_and_rename(instance, filename):
    upload_to = 'ads/photos'
    ext = filename.split('.')[-1]
    filename = f'{uuid4().hex}.{ext}'

    return os.path.join(upload_to, filename)


class Photo(models.Model):
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return f'Для объявления - {self.ad}'

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Model(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Generation(models.Model):
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarParameter(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Body(CarParameter):
    class Meta:
        verbose_name_plural = 'Bodies'
    pass

class EngineType(CarParameter):
    pass

class BoostType(CarParameter):
    pass

class Drive(CarParameter):
    pass

class Broken(CarParameter):
    class Meta:
        verbose_name_plural = 'Broken'
    pass