from django.contrib import admin
from core.admin import BaseAdmin

from .models import Hotel, Rate

class HotelAdmin(BaseAdmin, admin.ModelAdmin):
    list_filter = ('country', 'created_by', 'modified_by')
    search_fields = ('name', 'child_with_bed_rate', 'child_without_bed_rate', 'adult_breakfast_rate')
    list_display = ('name', 'country',  \
            'child_with_bed_rate', 'child_without_bed_rate', 'adult_breakfast_rate',\
            'date_created', 'date_modified', 'created_by', 'modified_by')
    exclude = ('created_by', 'modified_by')

class RateAdmin(BaseAdmin, admin.ModelAdmin):
    list_filter = ('hotel', 'room', 'date_from_day', 'date_from_month', 'date_to_day', 'date_to_month', 'created_by', 'modified_by')
    list_display = ('hotel', 'room', 'rate', \
            'date_from_day', 'date_from_month', 'date_to_day', 'date_to_month',\
            'date_created', 'date_modified', 'created_by', 'modified_by')
    exclude = ('created_by', 'modified_by')


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Rate, RateAdmin)
