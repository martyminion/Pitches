import unittest
from app.models import User,Pitches,Comments,Category
from app import db

class TestPitches(unittest.TestCase):
  '''
  this will test the other models in the app
  '''

  def setUp(self):
    '''
    runs for every test to set up the bd
    '''
    #User
    self.user_John = User(username = "John", email='John@gmail.com', prof_pic="profilepic/path",bio = 'This is just the beginning',password = 'potato' )
    
    #Comments
    self.test_comment = Comments(comment = "This is awsome", user_id = 1, pitch_id = 1)
  
    #Category
    self.test_category = Category(name = "Flirty", description = "Get a Bae")

    #Pitches
    self.test_pitch = Pitches(title = "Home", pitch = "East or West",user_id = 1, category_id = 1, up_votes = 3, down_votes = 2)

    db.session.add(self.user_John,self.test_comment)
    db.session.add(self.test_category,self.test_pitch)
    db.session.commit()

  def tearDown(self):
    '''
    runs after each test is run
    '''
    Comments.query.delete()
    Pitches.query.delete()
    User.query.delete()
    db.session.commit()

  def test_correct_instantiation(self):

    #Comments
    self.assertEqual(self.test_comment.comment,"This is awsome")
    self.assertEqual(self.test_comment.user_id,1)
    self.assertEqual(self.test_comment.pitch_id,1)
    #Category
    self.assertEqual(self.test_category.name,'Flirty')
    self.assertEqual(self.test_category.description,'Get a Bae')
    #Pitches
    self.assertEqual(self.test_pitch.title,"Home")
    self.assertEqual(self.test_pitch.pitch,"East or West")
    self.assertEqual(self.test_pitch.user_id,1)
    self.assertEqual(self.test_pitch.category_id,1)
    self.assertEqual(self.test_pitch.up_votes,3)
    self.assertEqual(self.test_pitch.down_votes,2)
    
  def test_get_categoryid(self):
    self.assertEqual(self.test_category.get_categoryid('Flirty'),10)

  def test_get_pitches_by_category(self):
    self.assertTrue(self.test_pitch.get_pitches_by_category(10) is not None)

  def test_get_pitches_by_user(self):
    self.assertTrue(self.test_pitch.get_pitches_by_user(1) is not None)

  def test_get_comments_by_pitch(self):
    self.assertTrue(self.test_comment.get_comments_by_pitch(14) is not None)

  