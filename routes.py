from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from ext import db, login_manager
from models import News, User
from forms import NewsForm, RegisterForm, LoginForm


main = Blueprint("main", __name__)


# =========================
# USER LOADER (Flask-Login)
# =========================
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# =========================
# HOME PAGE
# =========================
@main.route("/")
def home():

    latest_news = (
        News.query
        .order_by(News.created_at.desc())
        .limit(3)
        .all()
    )

    return render_template(
        "home.html",
        news=latest_news
    )


# =========================
# ALL NEWS
# =========================
@main.route("/news")
def news():

    news_list = (
        News.query
        .order_by(News.created_at.desc())
        .all()
    )

    return render_template(
        "news.html",
        news=news_list
    )


# =========================
# NEWS DETAILS
# =========================
@main.route("/news/<int:news_id>")
def news_detail(news_id):

    news = News.query.get_or_404(news_id)

    return render_template(
        "news_detail.html",
        news=news
    )


# =========================
# ADD NEWS (WTForms)
# =========================
@main.route("/add-news", methods=["GET", "POST"])
@login_required
def add_news():

    form = NewsForm()

    if form.validate_on_submit():

        new_news = News(

            title=form.title.data,

            category=form.category.data,

            author=form.author.data,

            image=form.image.data,

            description=form.description.data
        )


        db.session.add(new_news)

        db.session.commit()


        return redirect(
            url_for("main.news")
        )


    return render_template(
        "add_news.html",
        form=form
    )


# =========================
# EDIT NEWS
# =========================
@main.route(
    "/edit-news/<int:news_id>",
    methods=["GET", "POST"]
)
@login_required
def edit_news(news_id):

    news = News.query.get_or_404(news_id)


    if request.method == "POST":

        news.title = request.form["title"]

        news.category = request.form["category"]

        news.author = request.form["author"]

        news.image = request.form["image"]

        news.description = request.form["description"]


        db.session.commit()


        return redirect(
            url_for(
                "main.news_detail",
                news_id=news.id
            )
        )


    return render_template(
        "edit_news.html",
        news=news
    )



# =========================
# DELETE NEWS
# =========================
@main.route("/delete-news/<int:news_id>")
@login_required
def delete_news(news_id):

    news = News.query.get_or_404(news_id)


    db.session.delete(news)

    db.session.commit()


    return redirect(
        url_for("main.news")
    )



# =========================
# REGISTER
# =========================
@main.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    form = RegisterForm()


    if form.validate_on_submit():

        user = User(
            username=form.username.data
        )


        user.set_password(
            form.password.data
        )


        db.session.add(user)

        db.session.commit()


        return redirect(
            url_for("main.login")
        )


    return render_template(
        "register.html",
        form=form
    )



# =========================
# LOGIN
# =========================
@main.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    form = LoginForm()


    if form.validate_on_submit():

        user = User.query.filter_by(
            username=form.username.data
        ).first()


        if user and user.check_password(
            form.password.data
        ):

            login_user(user)


            return redirect(
                url_for("main.home")
            )


    return render_template(
        "login.html",
        form=form
    )



# =========================
# LOGOUT
# =========================
@main.route("/logout")
@login_required
def logout():

    logout_user()


    return redirect(
        url_for("main.home")
    )



# =========================
# ABOUT PAGE
# =========================
@main.route("/about")
def about():

    return render_template(
        "about.html"
    )