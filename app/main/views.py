from flask import render_template,redirect,request,url_for,abort
from . import main
from ..models import Pitches,User,Comments,Category
from .. import db
from flask_login import login_required

@main.route('/')
def index():
  '''
  returns the index page and its data which is the pitches arranged by category
  '''
  pitches_funny = Pitches.get_pitches_by_category(1)
  pitches_flirty = Pitches.get_pitches_by_category(2)

  return render_template('index.html',flirty = pitches_flirty, funny = pitches_funny)

@main.route('/user/<uname>')
def profile(uname):
  '''
  defines the function to display a user profile

  args: username

  returns: users pitches
  '''
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)
  
  pitches_uname = Pitches.get_pitches_by_user(user.id)
  

  return render_template('profile/profile.html',user = user, userPitches = pitches_uname)