from django.db import models


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