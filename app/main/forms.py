from flask import render_template,redirect,request,url_for,abort
from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField
from wtforms import ValidationError
from wtforms.validators import Required
from ..models import User

class UpdateProfile(FlaskForm):
  '''
  if user wants to update their user Bio
  '''
  bio = TextAreaField('Update Your Bio')
  submit = SubmitField('Update')
  