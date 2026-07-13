from flask import Flask
from ext import db, login_manager
from routes import main


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "technewsgeorgia2026"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///news.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)

    login_manager.init_app(app)


    app.register_blueprint(main)


    with app.app_context():
        db.create_all()


    return app