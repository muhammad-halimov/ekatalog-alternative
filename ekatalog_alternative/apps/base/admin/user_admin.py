from django.contrib import admin
from ekatalog_alternative.apps.base.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = User.DisplayFields
    search_fields = User.SearchableFields
    list_filter = User.FilterFields
