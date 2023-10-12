from curses import flash
from flask import redirect, render_template, url_for
from flask_login import LoginManager, current_user, login_required, logout_user
import app

@LoginManager.user_loader
def load_user(user_id):
    return app.User.query.get(int(user_id))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "Thankx for visiting!")
    return redirect(url_for("login"))