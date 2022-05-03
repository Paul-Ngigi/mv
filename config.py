import os
import pymysql

class Config:
    """
    This is the most common way of adding your local db to your application
    """
    # SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/db_name' 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:pass12345@localhost/cinema' 
    SECRET_KEY  = '*318^&#GR!BRBCQKDNAHX*&@#WDBQN^#YBO'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}