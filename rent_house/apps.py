from django.apps import AppConfig


class RentHouseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "rent_house"

    def ready(self):
        import rent_house.signals
