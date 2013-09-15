from django.contrib import admin
from core.admin import BaseAdmin

from .models import Country, CountryDestination, Room, Transfer, ExchangeRate

class RoomAdmin(BaseAdmin, admin.ModelAdmin):
    list_filter = ( 'created_by', 'modified_by')
    list_display = ('name',  'date_created', 'date_modified', 'created_by', 'modified_by')
    exclude = ('created_by', 'modified_by')

class CountryAdmin(BaseAdmin, admin.ModelAdmin):
    list_filter = ( 'created_by', 'modified_by')
    list_display = ('code', 'name',  'date_created', 'date_modified', 'created_by', 'modified_by')
    exclude = ('created_by', 'modified_by')

class CountryDestinationAdmin(BaseAdmin, admin.ModelAdmin):
    list_filter = ( 'created_by', 'modified_by')
    list_display = ('code', 'name',  'country', 'date_created', 'date_modified', 'created_by', 'modified_by')
    exclude = ('created_by', 'modified_by')

class TransferAdmin(BaseAdmin, admin.ModelAdmin):
    list_filter = ( 'created_by', 'modified_by')
    list_display = ('name', 'rate',  'date_created', 'date_modified', 'created_by', 'modified_by')
    exclude = ('created_by', 'modified_by')

class ExchangeRateAdmin(BaseAdmin, admin.ModelAdmin):
    list_filter = ( 'created_by', 'modified_by')
    list_display = ('rate', 'date_from', 'date_to',  'date_created', 'date_modified', 'created_by', 'modified_by')
    exclude = ('created_by', 'modified_by')

admin.site.register(Room, RoomAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(CountryDestination, CountryDestinationAdmin)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)
