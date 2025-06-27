from django.contrib import admin
from ekatalog_alternative.apps.base.models.shop import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = Shop.DisplayFields
    search_fields = Shop.SearchableFields
    list_filter = Shop.FilterFields
