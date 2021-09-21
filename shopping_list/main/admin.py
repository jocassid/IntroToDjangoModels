from django.contrib import admin
from .models import \
    Store, \
    StoreType


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(StoreType)
class StoreTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
