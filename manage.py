from app import create_app,db
from flask_script import Manager, Server,Shell
from app.models import User,Pitches,Comments,Category
from flask_migrate import Migrate, MigrateCommand


#create an app instance
app = create_app('test')
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
  '''
  Running the unit Tests
  '''
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User = User,Pitches = Pitches,Comments = Comments,Category=Category )
if __name__ == '__main__':
  manager.run()