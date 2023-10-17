from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user
from models import User
from auth.init import auth


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        remember = bool(request.form.get("remember"))

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            if user.role in ("developer", "teacher"):
                login_user(user, remember=remember)
                flash("Successfully logged in!", "success")
                return redirect(url_for("dashboard.dashboard"))  # Adjust the target route accordingly
            else:
                flash("You are not authorized to access the dashboard.", "danger")
        else:
            flash("Please check your credentials.", "danger")

    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "Thank you for visiting!")
    return redirect(url_for("auth.login"))
