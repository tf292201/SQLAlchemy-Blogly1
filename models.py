from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=True, default='https://www.freeiconspng.com/uploads/blue-user-icon-32.jpg')

    def __repr__(self):
        """Show info about user."""
        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"
<<<<<<< Updated upstream
=======

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('Users', backref='posts')

    
    def __repr__(self):
        """Show info about post."""
        p = self
        return f"<Post {p.id} {p.title} {p.content} {p.created_at} {p.user_id}>"

class Tags(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    tagged_posts = db.relationship(
        'Posts',
        secondary="posts_tags",  
        backref="tags",
    )

    def __repr__(self):
        """Show info about tag."""
        t = self
        return f"<Tag {t.id} {t.name}>"

class PostsTags(db.Model):
    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

    def __repr__(self):
        """Show info about posttag."""
        pt = self
        return f"<PostTag {pt.post_id} {pt.tag_id}>"
>>>>>>> Stashed changes
