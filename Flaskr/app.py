from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from auth.init import auth
from models import db
import capture

app = Flask(__name__)
app.config["SECRET_KEY"] = "#1*6j!a&a3i8$d##p!!"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dblogs.db"
db = SQLAlchemy(app)


# Creating user model for basic authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="user")

# Create the database tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Welcome to the Home Page"

# Registering the auth blueprint
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(capture.capture_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
