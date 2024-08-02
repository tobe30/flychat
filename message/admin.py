from django.apps import AppConfig

# Register your models here.

class MessageConfig(AppConfig):
    defaul_auto_field = 'django.db.models.BigAutoField'
    name = 'message'

