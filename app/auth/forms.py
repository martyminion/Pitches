from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms import ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
  '''
  user registration form
  '''
  email = StringField('Please Enter Your Email Address', validators=[Required(),Email()])
  username = StringField('Enter a cool username',validators=[Required()])
  bio = TextAreaField('Tell us a bit about yourseld')
  password = PasswordField('A password you can remember',validators=[Required(),EqualTo('password_confirm',message="Password must match")])
  password_confirm = PasswordField('Can you remember your password'validators=[Required()])
  submit = SubmitField('You can join us now')

  #custom validators
  def validate_email(self,data_field):
    '''
    checks if there's an account with the same email
    '''
    if User.query.filter_by(email = data_field.data).first():
      raise ValidationError('You are already one of us')

  def validate_username(self,data_field):
    '''
    checks if the username exists
    '''
    if User.query.filter_by(username = data_field.data).first():
      raise ValidationError("Shucks! This cool name is already taken")