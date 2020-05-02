from flask import render_template,redirect,request,url_for,abort
from . import main
from ..models import Pitches,User,Comments,Category
from .. import db

@main.route('/')
def index():
  '''
  returns the index page and its data
  '''
  message = "We have began"
  return render_template('index.html',message = message)