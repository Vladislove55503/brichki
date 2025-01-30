from django.contrib import admin

from .models import Brand, Model, Generation


admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Generation)