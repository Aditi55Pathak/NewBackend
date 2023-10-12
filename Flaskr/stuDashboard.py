from flask import Blueprint, render_template
from flask_login import login_required, current_user

student_data = Blueprint('student_data', __name__)

@student_data.route("/dashboard/student_data", methods=["GET"])
@login_required
def student_data():
    if current_user.role in ("developer", "teacher"):
        # Drop your AI-ML code for fetching data from the dataset
        students = [
            {"id": 1, "name": "Student 1", "roll_number": "001"},
            {"id": 2, "name": "Student 2", "roll_number": "002"},
            # Add more student data dictionaries as needed
        ]
        # Render the student_data.html template with the student data
        return render_template("student_data.html", students=students)
    else:
        return "You are not authorized to access student data."

