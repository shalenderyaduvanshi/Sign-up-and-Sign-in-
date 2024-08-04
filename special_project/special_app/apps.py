from django.apps import AppConfig


class SpecialAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'special_app'
