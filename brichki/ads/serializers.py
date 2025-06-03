from .models import (
    Ad, Brand, Model, Generation, EngineType, BoostType, Drive, Body,
    )
from rest_framework import serializers


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            'brand', 'model', 'generation', 'engine_type', 'boost_type', 
            'drive', 'body', 'mileage', 'price',
            ]
        depth = 1