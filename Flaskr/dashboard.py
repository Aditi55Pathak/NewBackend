from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/dashboard")
@login_required
def dashboard():
    if current_user.role in ("developer", "teacher"):
        return render_template("dashboard.html")
    else:
        return "You are not authorized to access this page."

