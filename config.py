import os

class Config():
  '''
  defines the class that contains all general requirements
  '''
  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST = 'app/static/images'

  #settig up Simple mde configurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True
  #email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
class ProdConfig(Config):
  DEBUG=False

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://martin:kimani@localhost/pitches"
  DEBUG=True

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://martin:kimani@localhost/pitches_test"
  DEBUG=True
  
config_options = {
  'development':DevConfig,
  'production' :ProdConfig,
  'test':TestConfig
}
