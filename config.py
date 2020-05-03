
class Config():
  '''
  defines the class that contains all general requirements
  '''
  SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://martin:kimani@localhost/pitches"
  SECRET_KEY = 'ghostRider'
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
