from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import RegistrationForm
from .models import User, db

register = Blueprint('register', __name__)

@register.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_exists = User.query.filter_by(username=form.username.data).first()
        if user_exists:
            flash("Username already taken.", "danger")
            return render_template("register.html", form=form)

        valid_roles = ("user", "developer", "teacher")
        if form.role.data in valid_roles:
            user = User(username=form.username.data, password=form.password.data, role=form.role.data)
            db.session.add(user)
            db.session.commit()
            flash("Successfully registered", "success")
            return redirect(url_for("login.login"))
        else:
            flash("Invalid role selected.", "danger")
    return render_template("register.html", form=form)

