from django.contrib import admin

from .models import (Ad, Photo, Brand, Model, Generation, 
					 Body, EngineType, BoostType, Drive, Broken)

# Register your models here.

admin.site.register(Ad)
admin.site.register(Photo)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Generation)
admin.site.register(Body)
admin.site.register(EngineType)
admin.site.register(BoostType)
admin.site.register(Drive)
admin.site.register(Broken)