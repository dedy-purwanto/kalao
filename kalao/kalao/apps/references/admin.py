from django.contrib import admin
from core.admin import BaseAdmin

from .models import Country, CountryDestination

class CountryAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = ('code', 'name', 'active', 'date_created', 'date_modified', 'created_by', 'modified_by')
    exclude = ('created_by', 'modified_by')

class CountryDestinationAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = ('code', 'name', 'active', 'country', 'date_created', 'date_modified', 'created_by', 'modified_by')
    exclude = ('created_by', 'modified_by')

admin.site.register(Country, CountryAdmin)
admin.site.register(CountryDestination, CountryDestinationAdmin)
