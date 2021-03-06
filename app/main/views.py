from flask import render_template,redirect,request,url_for,abort
from . import main
from ..models import Pitches,User,Comments,Category
from .. import db,photos
from flask_login import login_required,current_user
from .forms import UpdateProfile,NewPitch,NewComment
import markdown2
from sqlalchemy import desc

@main.route('/')
def index():
  '''
  returns the index page and its data which is the pitches arranged by category
  '''
  pitches_flirty = Pitches.get_pitches_by_category(1) #had started from 3 for local to work
  pitches_standup = Pitches.get_pitches_by_category(2)
  pitches_religious = Pitches.get_pitches_by_category(3)
  pitches_product = Pitches.get_pitches_by_category(4)
  pitches_interview = Pitches.get_pitches_by_category(5)
  pitches_zen = Pitches.get_pitches_by_category(6)
  pitches_Anime = Pitches.get_pitches_by_category(7)

  return render_template('index.html',anime = pitches_Anime, zen = pitches_zen,flirty = pitches_flirty, standup = pitches_standup,religious = pitches_religious,product= pitches_product,interview = pitches_interview)

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


@main.route('/user/<uname>/new/pitch',methods = ['GET','POST'])
@login_required
def new_pitch(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)
  form = NewPitch()

  if form.validate_on_submit():
    categoryId = Category.get_categoryid(form.category.data)
    add_pitch = Pitches(title = form.title.data, pitch = form.pitch.data, category_id = categoryId, user_id = user.id,up_votes = 0,down_votes = 0)
    db.session.add(add_pitch)
    db.session.commit()
    return redirect(url_for('.profile',uname = uname))
  
  title = "New Pitch"
  
  return render_template('addPitch.html', title = title, form = form)

@main.route('/pitch/<int:id>')
@login_required
def single_pitch(id):
  
  pitchnew = Pitches.query.get(id)
  if pitchnew is None:
    abort(404)
  
  format_pitch = markdown2.markdown(pitchnew.pitch, extras=["code-friendly",'fenced_code_blocks'])
  
  return render_template('pitch.html', pitchnew = pitchnew, format_pitch = format_pitch)

@main.route('/<int:pitchId>/<uname>/comment',methods=['GET','POST'])
@login_required
def pitch_comment(uname,pitchId):
  user = User.query.filter_by(username = uname).first()
  pitch = Pitches.query.filter_by(id = pitchId).first()
  if user is None:
    abort(404)
  form = NewComment()

  if form.validate_on_submit():
    new_comment = Comments(comment = form.comment.data, user_id = user.id, pitch_id = pitchId)
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for('.index'))

  comment_list = Comments.get_comments_by_pitch(pitchId)
  
  title = "New Comment"
  return render_template('addcomment.html',title = title, form = form, CommentPitch = pitch,comment_list = comment_list)


@main.route('/pitch/upvote/<int:pitch_id>')
def upvote(pitch_id):
  pitch = Pitches.query.filter_by(id = pitch_id).first()
  
  new_upvote_no = pitch.up_votes + 1
  
  pitch.up_votes = new_upvote_no
  db.session.commit()
  
  return redirect(url_for('.index'))

@main.route('/pitch/downvote/<int:pitch_id>')
def downvote(pitch_id):
  pitch = Pitches.query.filter_by(id = pitch_id).first()
  
  new_upvote_no = pitch.down_votes + 1
  
  pitch.down_votes = new_upvote_no
  db.session.commit()
  
  return redirect(url_for('.index'))