from flask import render_template,redirect,request,url_for,abort
from . import main
from ..models import Pitches,User,Comments,Category
from .. import db

@main.route('/')
def index():
  '''
  returns the index page and its data
  '''
  pitches_funny = Pitches.get_pitches_by_category(1)
  pitches_flirty = Pitches.get_pitches_by_category(2)

  return render_template('index.html',flirty = pitches_flirty, funny = pitches_funny)

