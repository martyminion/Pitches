import os

class Config():
  '''
  defines the class that contains all general requirements
  '''
  SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://martin:kimani@localhost/pitches"
  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST = 'app/static/images'

  #email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
class ProdConfig(Config):
  DEBUG=False

class DevConfig(Config):
  DEBUG=True

class TestConfig(Config):
  pass
config_options = {
  'development':DevConfig,
  'production' :ProdConfig,
  'test':TestConfig
}
