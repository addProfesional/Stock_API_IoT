from ..models.AppConfigModel import AppConfigModel

class AppConfig:
    @staticmethod
    def get_config():

        config =  AppConfigModel.query.all().pop()
        return config