class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "dhflkjahskjfsadf"

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):

    pass

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql://moringa:jimi@localhost:5432/pomodoro'

    DEBUG = True

config_options = {
'development' : DevConfig,
'production' : ProdConfig

}
