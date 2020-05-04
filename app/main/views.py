from flask import render_template,redirect,request,url_for,abort
from . import main
from ..models import Pitches,User,Comments,Category
from .. import db,photos
from flask_login import login_required,current_user
from .forms import UpdateProfile

@main.route('/')
def index():
  '''
  returns the index page and its data which is the pitches arranged by category
  '''
  pitches_funny = Pitches.get_pitches_by_category(2)
  pitches_flirty = Pitches.get_pitches_by_category(1)

  return render_template('index.html',flirty = pitches_flirty, funny = pitches_funny)

@main.route('/user/<uname>')
@login_required
def profile(uname):
  '''
  defines the function to display a user profile

  args: username

  returns: users pitches
  '''
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)
  
  pitches_uname = Pitches.get_pitches_by_user(user.id)
  

  return render_template('profile/profile.html',user = user, userPitches = pitches_uname)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def bio_update(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)
  
  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()
    return redirect(url_for('.profile',uname = user.username))
  return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()

  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'images/{filename}'
    user.prof_pic = path
    db.session.commit()
  return redirect(url_for('main.profile',uname = uname))
# @main.route('/pitch/upvote/<int:pitch_id>')
# @login_required
# def upvote(pitch_id):

#   pitch = Pitches.query.filter_by(id = pitch_id).first()
#   
#   # new_upvote_no = pitch.up_votes + 1
#   # 
#   # 
#   # pitch.up_votes = new_upvote_no
#   # db.session.add(pitch)
#   # db.session.commit()
  
#   return redirect(url_for('.index')upvotes_no = new_upvote_no)