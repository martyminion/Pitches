from flask import render_template,redirect,request,url_for,abort
from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,IntegerField
from wtforms import ValidationError
from wtforms.validators import Required
from ..models import User

class UpdateProfile(FlaskForm):
  '''
  if user wants to update their user Bio
  '''
  bio = TextAreaField('Update Your Bio')
  submit = SubmitField('Update')

class NewPitch(FlaskForm):
  '''
  adds a new pitch
  '''
  title = StringField('Title',validators=[Required()])
  category = IntegerField('Enter Category ID',validators=[Required()])
  pitch = TextAreaField('You have one minute to be awesome..')
  submit = SubmitField('Add')

class NewComment(FlaskForm):
  '''
  adds a new comment
  '''
  comment = TextAreaField('Be Nice with Feedback',validators=[Required()])
  submit = SubmitField('Add')