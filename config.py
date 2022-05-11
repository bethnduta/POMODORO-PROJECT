class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):

    pass

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jimi@localhost/pomodoro'

    DEBUG = True

config_options = {
'development' : DevConfig,
'production' : ProdConfig

}
