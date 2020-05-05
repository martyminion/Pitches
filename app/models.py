from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy import desc
class User(UserMixin,db.Model):
  '''
  this class defines the user characteristics
  '''
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255),index = True)
  email = db.Column(db.String(255),unique = True, index = True)
  prof_pic = db.Column(db.String())
  bio = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))

  comments = db.relationship('Comments',backref = 'username', lazy = 'dynamic')
  pitches = db.relationship('Pitches',backref = 'username', lazy = 'dynamic')

  @property #creates a write only class
  def password(self):
    raise AttributeError('You cannot read the password property')

  @password.setter
  def password(self,password):
    '''
    takes the password and generates a hash value from it which is what we store
    '''
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    '''
    checks if the hash of the password entered matches the hash stored
    '''
    return check_password_hash(self.pass_secure,password)

  @login_manager.user_loader
  def load_user(user_id):
    '''
    call back function that retrieves a user when a unique identifier is passed
    '''
    return User.query.get(int(user_id))



  def __repr__(self):
    return f'User {self.username}'

class  Comments(db.Model):
  '''
  this class defines characteristics of a comment
  '''
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key = True)
  comment = db.Column(db.String(255))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

  def save_comments(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments_by_pitch(cls,id):
    '''
    function to retrieve comments based on the pitch_id
    '''
    comments_list = Comments.query.filter_by(pitch_id = id).all()

    return comments_list

  def __repr__(self):
    return f'Comment {self.comment}'
  
class  Pitches(db.Model):
  '''
  this class defines characteristics of a pitch
  '''
  __tablename__ = 'pitches'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  pitch = db.Column(db.String)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
  up_votes = db.Column(db.Integer)
  down_votes = db.Column(db.Integer)

  comments = db.relationship('Comments',backref = 'pitch', lazy = 'dynamic')

  def save_pitches(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_pitches_by_user(cls,id):
    '''
    function to retrieve pitches based on the user_id
    '''
    pitches_list = Pitches.query.filter_by(user_id = id).order_by(desc(Pitches.id)).all()
   

    return pitches_list

  @classmethod
  def get_pitches_by_category(cls,categoryId):
    '''
    function to retrieve pitches based on the category
    '''

    pitch_list = Pitches.query.filter_by(category_id = categoryId).order_by(desc(Pitches.id)).all()

    return pitch_list
  @classmethod
  def get_upvotes(cls,pitch_id):
    '''
    gets the upvotes of a particular pitch
    '''
    upvotes_number = Pitches.query.filter_by(id = pitch_id).first()
    return upvotes_number.up_votes

  @classmethod
  def get_downvotes(cls,pitch_id):
    '''
    gets the downvotes of a particular pitch
    '''
    downvotes_number = Pitches.query.filter_by(id = pitch_id).first()
    return downvotes_number.down_votes

  def __repr__(self):
    return f'Pitch {self.title}'

class  Category(db.Model):
  '''
  this class defines the categories
  '''
  __tablename__ = 'categories'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  description = db.Column(db.String(255))

  pitches = db.relationship('Pitches',backref = 'name', lazy = 'dynamic')

  @classmethod
  def get_categoryid(cls,categoryname):
    '''
    returns the category id on getting a category name
    '''
    category_id = Category.query.filter_by(name = categoryname ).first()

    return category_id.id

  def __repr__(self):
    return f'Category {self.name}'