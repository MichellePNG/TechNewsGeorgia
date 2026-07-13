from datetime import datetime
from ext import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class News(db.Model):

    __tablename__ = "news"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    author = db.Column(
        db.String(100),
        nullable=False
    )

    image = db.Column(
        db.String(500),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



class User(db.Model, UserMixin):

    __tablename__ = "users"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )


    password = db.Column(
        db.String(200),
        nullable=False
    )


    is_admin = db.Column(
        db.Boolean,
        default=False
    )


    def set_password(self, password):

        self.password = generate_password_hash(password)



    def check_password(self, password):

        return check_password_hash(
            self.password,
            password
        )