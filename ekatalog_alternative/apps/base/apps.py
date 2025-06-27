from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ekatalog_alternative.apps.base'  # Change this line
    verbose_name = 'Основная часть'
    verbose_name_plural = 'Основная часть'
