import unittest
from app.models import User

from app import db

class TestUser(unittest.TestCase):

  def setUp(self):
    '''
    this runs at the beginning of every test, sets Up the user instance
    '''
    self.user_John = User(username = "John", email='John@gmail.com', prof_pic="profilepic/path",bio = 'This is just the beginning',password = 'potato' )
    db.session.add(self.user_John)
    db.session.commit()
  def tearDown(self):
    '''
    runs to clear the information, dletes all the information after the test is done
    '''
    delete = User.query.delete()
    db.session.commit()

  def test_password_setter(self):
    self.assertTrue(self.user_John.pass_secure is not None)

  def test_check_instance_variables(self):
    '''
    confirm if the model is instantiated correctly
    '''
    self.assertEquals(self.user_John.username,"John")
    self.assertEquals(self.user_John.email,"John@gmail.com")
    self.assertEquals(self.user_John.prof_pic,"profilepic/path")
    self.assertEquals(self.user_John.bio,"This is just the beginning")
    self.assertTrue(self.user_John.verify_password('potato'))
  
  def test_no_access_passsword(self):
    with self.assertRaises(AttributeError):
      self.user_John.password

    
