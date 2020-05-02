from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app():
  app = Flask(__name__)

  #creating app configurations
  app.config.from_object(config_options[config_name])

  #Initialization of flask extensions
  bootstrap.init_app(app)

  #registering a blueprint
  from main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app
