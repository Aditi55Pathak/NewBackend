from flask import render_template
from flask_login import current_user, login_required
from app import app

# Mapping face using AI ML
@app.route("/dashboard/map_face", methods=["POST"])
@login_required
def map_face():
    if current_user.role in ("developer", "teacher"):
        # Put AI ML code here
        return "Face mapped successfully!"  # Return a success message
    else:
        return "You are not authorized to map a face."
