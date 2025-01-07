from django.db import models

from FILTER.models import Brand
from FILTER.models import Model
from FILTER.models import Generation


class Ads(models.Model):
    class Body(models.IntegerChoices):
        SEDAN = 0, 'Седан'
        HATCHBACK = 1, 'Хэтчбек'
        LIFTBACK = 2, 'Лифтбек'
        STATION_WAGON = 3, 'Универсал'
        MINIVAN_SERVICE = 4, 'Минивэн'
        COUPE = 5, 'Купе'
        PICKUP_TRUCK = 6, 'Пикап'
        CABRIOLET = 7, 'Кабриолет'
        VAN = 8, 'Фургон'
        SUV = 9, 'Внедорожник'

    class EngineType(models.IntegerChoices):
        GASOLINE = 0, 'Бензин'
        DIESEL = 1, 'Дизель'
        HYBRID = 2, 'Гибрид'
        ELECTRO = 3, 'Электро'

    class BoostType(models.IntegerChoices):
        NOT_PROVIDED = 0, 'Не предусмотрен'
        ATMOSPHERIC = 1, 'Атмосферный'
        TURBOCHARGED = 2, 'Турбированный'

    class EquipmentType(models.IntegerChoices):
        GAS_CYLINDER = 1, 'Газобаллонное оборудование'

    class Drive(models.IntegerChoices):
        FRONT_WHEEL = 0, 'Передний'
        REAR_WHEEL = 1, 'Задний'
        ALL_WHELL = 2, 'Полный'

    class Broken(models.IntegerChoices):
        NOT_BROKEN = 0, 'Не битая'
        BROKEN = 1, 'Битая'
        NOT_MOVE = 2, 'Не на ходу'


    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name='Марка')
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, verbose_name='Модель')
    generation = models.ForeignKey(Generation, on_delete=models.SET_NULL, null=True, verbose_name='Поколение')

    body = models.IntegerField(choices=Body.choices, verbose_name='Кузов')

    engine_type = models.IntegerField(choices=EngineType.choices, null=True, verbose_name='Двигатель')
    boost_type = models.IntegerField(choices=BoostType.choices, null=True, verbose_name='Нагнетатель')
    equipment_type = models.IntegerField(choices=EquipmentType.choices, null=True, blank=True, verbose_name='Дополнительное оборудование')

    engine_capacity = models.FloatField(verbose_name='Объём двигателя')
    drive = models.IntegerField(choices=Drive.choices, verbose_name='Привод')
    broken = models.IntegerField(choices=Broken.choices, verbose_name='Битая')
    mileage = models.IntegerField(default=0, verbose_name='Пробег')
    price = models.IntegerField(verbose_name='Цена')
    comment = models.CharField(max_length=10000, blank=True, default='', verbose_name='Комментарий')

    def __str__(self):
        return f'{self.brand}, {self.model}, {self.generation}, {self.engine_capacity}, {self.price}'