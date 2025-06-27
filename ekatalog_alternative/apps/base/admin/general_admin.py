from django.contrib import admin
from ekatalog_alternative.apps.base.models.general import General


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = General.DisplayFields
    search_fields = General.SearchableFields
    list_filter = General.FilterFields
