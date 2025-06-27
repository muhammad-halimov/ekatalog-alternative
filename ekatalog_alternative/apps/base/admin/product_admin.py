from django.contrib import admin
from ekatalog_alternative.apps.base.models.product import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = Product.DisplayFields
    search_fields = Product.SearchableFields
    list_filter = Product.FilterFields
