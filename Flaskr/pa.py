from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

present_absent_data = Blueprint('present_absent_data', __name__)

@present_absent_data.route("/dashboard/present_absent_data", methods=["GET", "POST"])
@login_required
def present_absent_data():
    if current_user.role in ("developer", "teacher"):
        if request.method == "POST":
            # Here, drop your code to capture an image and send it to your AI-ML model
            # and the model will determine the present/absent status and return the result
            # I took for example result='Present'
            result = 'Present'

            # It will render data to present_absent_data.html template
            return render_template("present_absent_data.html", result=result)
        else:
            # You can display the form to capture the image
            return render_template("capture_image.html")
    else:
        return "You are not authorized to access present/absent data."

