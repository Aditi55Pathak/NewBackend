from wtforms.validators import DataRequired, EqualTo, Length
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField
from flask import Flask
from login import login

app = Flask(__name__)
app.config["SECRET_KEY"] = "#1*6j!a&a3i8$d##p!!"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dblogs.db"
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

# Creating user model for basic authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="user")

# Create the database tables
with app.app_context():
    db.create_all()

# Register the login Blueprint
from login import login
app.register_blueprint(login)

@app.route("/")
def home():
    return "Welcome to the Home Page"

# Creating registration modules
class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    role = SelectField("Role", choices=[("user", "User"), ("developer", "Developer"), ("teacher", "Teacher")])
    submit = SubmitField("Register")

# Creating Login modules
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

if __name__ == "__main__":
    app.run(
        debug=True
    )  # 