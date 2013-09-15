from django.contrib import admin
from core.admin import BaseAdmin

from .models import Package, PackageBatch, Remark, PackageHotel

class PackageBatchInline(admin.TabularInline):
    model = PackageBatch
    extra = 1
    exclude = ('created_by', 'modified_by')

class RemarkInline(admin.TabularInline):
    model = Remark
    extra = 1
    exclude = ('created_by', 'modified_by')

class PackageHotelInline(admin.TabularInline):
    model = PackageHotel
    extra = 1
    exclude = ('created_by', 'modified_by')

class PackageAdmin(BaseAdmin, admin.ModelAdmin):
    list_filter = ('package_hotels__hotel',  'created_by', 'modified_by')
    search_fields = ('name',)
    list_display = ('name',  'markup_amount', 'date_modified', 'created_by', 'modified_by')
    exclude = ('created_by', 'modified_by')

    inlines = (PackageBatchInline, PackageHotelInline, RemarkInline)

admin.site.register(Package, PackageAdmin)
