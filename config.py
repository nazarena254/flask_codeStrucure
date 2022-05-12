import os

class Config:
    # UPLOADED_PHOTOS_DEST ='app/static/photos'

    # API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL') OR Line 9
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://localHostMachineName:databasePassword@localhost:5432/databaseName'


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nancyngunjiri1:databasePassword@localhost:5432/databaseName'

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI=heroku DATABASE_URL in the Config Var  Add this when deploying
    pass


class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
