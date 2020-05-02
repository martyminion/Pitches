from . import db

class User(db.Model):
  '''
  this class defines the user characteristics
  '''
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True, index = True)
  prof_pic = db.Column(db.String())
  bio = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))

  comments = db.relationship('Comments',backref = 'user', lazy = 'dynamic')
  pitches = db.relationship('Pitches',backref = 'user', lazy = 'dynamic')

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

  comments = db.relationship('Comments',backref = 'pitch', lazy = 'dynamic')

  def save_pitches(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_pitches_by_user(cls,id):
    '''
    function to retrieve pitches based on the user_id
    '''
    pitches_list = Pitches.query.filter_by(user_id = id).all()

    return pitches_list

  @classmethod
  def get_pitches_by_category(cls,categoryId):
    '''
    function to retrieve pitches based on the category
    '''
    pitch_list = Pitches.query.filter_by(category_id = categoryId).all()

    return pitch_list

  

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

  def __repr__(self):
    return f'Category {self.name}'