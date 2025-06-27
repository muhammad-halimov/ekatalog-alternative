from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ekatalog_alternative.apps.api'
    verbose_name = 'Программный интерфейс/API'
    verbose_name_plural = 'Программный интерфейс/API'
