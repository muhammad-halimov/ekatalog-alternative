from django.contrib import admin
from ekatalog_alternative.apps.base.models.category import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = Category.DisplayFields
    search_fields = Category.SearchableFields
    list_filter = Category.FilterFields
