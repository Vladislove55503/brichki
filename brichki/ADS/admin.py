from django.contrib import admin

from .models import Ads, Photos


class PhotosInline(admin.StackedInline):
    model = Photos
    extra = 1

class AdsAdmin(admin.ModelAdmin):
    list_display = [
        'brand',
        'model',
        'generation',
        'engine_type',
        'boost_type',
        'engine_capacity',
        'body',
        'drive',
        'broken',
        'mileage',
        'price',
    ]

    fieldsets = [
        ('Name', {'fields': [
            'brand',
            'model',
            'generation',
        ]}),
        ('Engine', {'fields': [
            'engine_type',
            'boost_type',
            'engine_capacity',
        ]}),
        ('Other', {'fields': [
            'body',
            'drive',
            'broken',
            'mileage',
        ]}),
        ('User', {'fields': [
            'price',
            'comment',
        ]}),
    ]

    inlines = [PhotosInline]


admin.site.register(Ads, AdsAdmin)