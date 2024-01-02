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
