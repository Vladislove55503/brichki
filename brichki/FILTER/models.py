from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Model(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Generation(models.Model):
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)