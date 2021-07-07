from django.apps import AppConfig


class JaguareteappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jaguareteapp'

class StoreConfig(AppConfig):
    name = 'store'  
