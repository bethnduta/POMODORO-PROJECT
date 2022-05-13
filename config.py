class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "dhflkjahskjfsadf"
    SQLALCHEMY_DATABASE_URI = "postgresql://samuel:samuel@localhost:5432/pomodoro"

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://samuel:samuel@localhost:5432/pomodoro"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://samuel:samuel@localhost:5432/pomodoro"
    DEBUG = True

config_options = {
'development' : DevConfig,
'production' : ProdConfig

}
