from flask import render_template,redirect,request,url_for,abort
from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,IntegerField,SelectField
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
  category = SelectField('Choose Your Category',validators=[Required()],choices=[('flirty','flirty'),('standup','standup'),('religious','religious'),('product','product'),('interview','interview'),('zen','zen'),('Anime','Anime')])
  pitch = TextAreaField('You have one minute to be awesome..')
  submit = SubmitField('Add')

class NewComment(FlaskForm):
  '''
  adds a new comment
  '''
  comment = TextAreaField('Be Nice with Feedback',validators=[Required()])
  submit = SubmitField('Add')