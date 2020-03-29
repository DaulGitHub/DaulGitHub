class Config:

    PROTOCOL = "http"


class DevelopmentConfig(Config):

    DOMAIN = 'localhost'
    PORT = '5000'

    DB_NAME = 'urls'
    DB_USER = 'postgres'
    DB_HOST = 'localhost'
    DB_PASSWORD = '123456'