from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user

from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index", methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for("index"))
        else:
            flash('Invalid login.')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))


"""
@app.route("/test", defaults={'name': None}, methods=['GET'])
@app.route("/test/<name>", methods=['GET'])
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, usuário!"


# Forçar para receber um inteiro
@app.route("/user/<int:id>", methods=['GET'])
def user(id):
    return str(id)
"""
