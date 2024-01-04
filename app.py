from flask import Flask, request, redirect, render_template
from models import db, connect_db, Users, Posts

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

# Connect to the '/' route
@app.route('/')
def home():
  return redirect('/users')

@app.route('/users', methods=['GET'])
def list_users():
  users = Users.query.all()
  return render_template("user_list.html", users = users)

@app.route('/users/add_user', methods=['POST', 'GET'])
def add_user():
  if request.method == 'GET':
    return render_template('add_user.html')
  else:
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    new_user = Users(first_name = first_name, last_name = last_name, image_url = image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>', methods=['GET'])
def show_user(user_id):
  user = Users.query.get_or_404(user_id)
  return render_template('user_details.html', user = user)

@app.route('/users/<int:user_id>/edit', methods=['POST', 'GET'])
def edit_user(user_id):
  user = Users.query.get_or_404(user_id)
  if request.method == 'GET':
    return render_template('edit_user.html', user = user)
  else:
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST', 'GET'])
def delete_user(user_id):
  user = Users.query.get_or_404(user_id)
  db.session.delete(user)
  db.session.commit()
  return redirect('/users')

@app.route('/users/<int:user_id>/posts/new', methods=['POST','GET'])
def new_post(user_id):
  user = Users.query.get_or_404(user_id)
  if request.method == 'GET':
    return render_template('new_post.html', user = user)
  else:
    title = request.form['title']
    content = request.form['content']
    new_post = Posts(title = title, content = content, user_id = user_id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{user_id}')
  
@app.route('/posts/<int:post_id>', methods=['GET'])
def show_post(post_id):
    post = Posts.query.get_or_404(post_id)
    return render_template('post_details.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST','GET'])
def edit_post(post_id):
    post = Posts.query.get_or_404(post_id)
    if request.method == 'GET':
        return render_template('edit_post.html', post=post)
    else:
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(f'/users/{post.user_id}')

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Posts.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(f'/users/{post.user_id}')




if __name__ == '__main__':
  app.run()
