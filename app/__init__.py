from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)
mail = Mail()

def create_app(config_name):
  app = Flask(__name__)

  #creating app configurations
  app.config.from_object(config_options[config_name])

  #Initialization of flask extensions
  bootstrap.init_app(app)
  db.init_app(app)
  login_manager.init_app(app)
  #configure uploadSet
  configure_uploads(app,photos)
  #configure Mail properties
  mail.init_app(app)
  #registering a blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate') #adds a prefix to all the routes registered under that blueprint
 
  return app
