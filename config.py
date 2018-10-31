import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Parent Project environment configuration class."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = '\xa9\xc0w|\xae\rP\xa4\xbcg+\x9c"\xee{-\x14m\xb5\xd055j\x16'
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DATABASE = 'store_db'
    DEBUG = True
    TESTING = False
    ENVIRONMENT = 'development'

class TestingConfig(Config):
    """Configurations for Testing."""
    DATABASE = 'store_db_test'
    DEBUG = True
    TESTING = True
    ENVIRONMENT = 'testing'

class ProductionConfig(Config):
    """Configurations for Production."""
    DATABASE = ''
    DEBUG = False
    TESTING = False
    ENVIRONMENT = 'production'
    HOST = ''
    USER = ''
    PASSWORD = ''

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
