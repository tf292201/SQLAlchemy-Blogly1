from flask import Flask, request, redirect, render_template
<<<<<<< Updated upstream
from models import db, connect_db, Users
=======
from models import db, connect_db, Users, Posts, Tags, PostsTags
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
=======
@app.route('/users/<int:user_id>/posts/new', methods=['POST','GET'])
def new_post(user_id):
  user = Users.query.get_or_404(user_id)
  tags = Tags.query.all()
  if request.method == 'GET':
    return render_template('new_post.html', user=user, tags=tags)
  else:
    tag_ids = request.form.getlist('tags')
    tags = Tags.query.filter(Tags.id.in_(tag_ids)).all()
    title = request.form['title']
    content = request.form['content']
    new_post = Posts(title=title, content=content, user_id=user_id, tags=tags)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{user_id}')
  
@app.route('/posts/<int:post_id>', methods=['GET'])
def show_post(post_id):
    post = Posts.query.get_or_404(post_id)
    tags = post.tags
    return render_template('post_details.html', post=post, tags=tags)

@app.route('/posts/<int:post_id>/edit', methods=['POST','GET'])
def edit_post(post_id):
    post = Posts.query.get_or_404(post_id)
    selected_tags = post.tags 
    tags = Tags.query.all()
    if request.method == 'GET':
        return render_template('edit_post.html', post=post, tags=tags, selected_tags=selected_tags)
    else:
        tag_ids = [int(num) for num in request.form.getlist("tags")]
        post.tags = Tags.query.filter(Tags.id.in_(tag_ids)).all()
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

@app.route('/tags', methods=['GET'])
def list_tags():
    tags = Tags.query.all()
    return render_template('tags_list.html', tags=tags)

@app.route('/tags/<int:tag_id>', methods=['GET'])
def show_tag(tag_id,):
    tag = Tags.query.get_or_404(tag_id)
    associated_posts = tag.tagged_posts
    return render_template('tag_details.html', tag=tag, posts=associated_posts)

@app.route('/tags/new', methods=['POST','GET'])
def new_tag():
    if request.method == 'GET':
        return render_template('new_tag.html')
    else:
        name = request.form['name']
        new_tag = Tags(name=name)
        db.session.add(new_tag)
        db.session.commit()
        return redirect('/tags')

@app.route('/tags/<int:tag_id>/edit', methods=['POST','GET'])
def edit_tag(tag_id):
    tag = Tags.query.get_or_404(tag_id)
    if request.method == 'GET':
        return render_template('edit_tag.html', tag=tag)
    else:
        tag.name = request.form['name']
        db.session.commit()
        return redirect('/tags')

@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
    tag = Tags.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return redirect('/tags')
>>>>>>> Stashed changes


if __name__ == '__main__':
  app.run()
