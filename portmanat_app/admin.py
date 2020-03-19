from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['imei_code', 'longitude', 'latitude', 'battery']


@admin.register(MobileData)
class MobileDataAdmin(admin.ModelAdmin):
    list_display = ['imei_code', 'longitude', 'latitude', 'battery']