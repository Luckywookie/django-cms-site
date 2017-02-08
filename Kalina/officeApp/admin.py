from django.contrib import admin
from .models import OfficeItem


class AdminOffice(admin.ModelAdmin):
    list_display = ('number', 'floor', 'is_free')


admin.site.register(OfficeItem, AdminOffice)
