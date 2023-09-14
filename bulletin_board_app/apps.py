from django.apps import AppConfig


class bulletin_board_appConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bulletin_board_app'

    def ready(self):
        import bulletin_board_app.signals