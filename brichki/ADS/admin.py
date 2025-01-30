from django.contrib import admin

from .models import Ads, Photos, Comments


admin.site.register(Ads)
admin.site.register(Photos)
admin.site.register(Comments)