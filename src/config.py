class Config:
    SECRET_KEY = '4Uc01'

#Configuracion de desarollo
class DevelomentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'sql10.freesqldatabase.com'
    MYSQL_USER = 'sql10511207'
    MYSQL_PASSWORD = 'kYFTyGWvH3'
    MYSQL_DB = 'sql10511207'


config = {
    'development': DevelomentConfig,
}




