from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from wtforms.validators import DataRequired, EqualTo, Length
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField

from Flaskr.app import LoginForm, User
# from .forms import LoginForm
# from .models import User

login = Blueprint('login', __name__)

@login.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            if user.role in ("developer", "teacher"):
                login_user(user, remember=form.remember.data)
                flash("Successfully logged in!", "success")
                return redirect(url_for("dashboard.dashboard"))
            else:
                flash("You are not authorized to access the dashboard.", "danger")
        else:
            flash("Please check your credentials.", "danger")
    return render_template("login.html", form=form)

@login.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "Thank you for visiting!")
    return redirect(url_for("login.login"))

