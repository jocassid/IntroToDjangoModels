from django.contrib import admin
from .models import \
    Item, \
    Store, \
    StoreType


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'store_type')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(StoreType)
class StoreTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
