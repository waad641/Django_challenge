# Import the AppConfig class from the django.apps module
from django.apps import AppConfig

# Create a configuration class for the 'producer_app' Django app
class ProducerAppConfig(AppConfig):
    # Specify the default auto-generated primary key field for models
    default_auto_field = 'django.db.models.BigAutoField'

    # Set the name of the Django app to 'producer_app'
    name = 'producer_app'
