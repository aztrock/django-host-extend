# vim: set expandtab ts=4 sw=4:
from django.contrib import admin
from django_host_extend.models import HostExtendModel

class HostExtendAdmin(admin.ModelAdmin):
    list_display = ('host', 'is_active', 'image', )
    fields = ('host', 'is_active', 'image', )
    list_filter = ('is_active', )
    search_fields = ('host','is_active', 'image', )


admin.site.register(HostExtendModel, HostExtendAdmin)
