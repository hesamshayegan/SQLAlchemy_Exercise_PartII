"""Models for Blogly."""

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app): 
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://icons.iconarchive.com/icons/icons8/ios7/256/Messaging-Happy-icon.png"

# it inherits from db
class User(db.Model):
    """ User. """
    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True)
                #    autoincrement=True)
    
    first_name = db.Column(db.Text,
                    nullable=False,
                    )
    
    last_name = db.Column(db.Text,
                    nullable=False,
                    )
    
    image_url = db.Column(db.Text,
                    nullable=False,
                    default=DEFAULT_IMAGE_URL)
    
    # Using of the keyword "backref" intead of using one relationship for User and another for Post
    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """ Return full name of user."""

        return f"{self.first_name} {self.last_name}"
    
#######################################################
# Blog posts model

class Post(db.Model):
    """ Blog post. """

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    # users is the name of the table not class
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
 
    @property
    def friendly_date(self):
        """ Return nicely-formatted date. """

        return self.created_at.strftime("%a %b %-d %Y %-I:%M %p")