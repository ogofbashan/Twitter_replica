from app import app, db
from app.models import User
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class PostForm(FlaskForm):
    tweet = StringField('What are you doing?', validators=[DataRequired(), Length(max=140)])
    submit = SubmitField('Tweet')

class TitleForm(FlaskForm):
    title = StringField("Enter a new header:", validators=[DataRequired()])
    submit = SubmitField('Change Title')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')

class LoginForm(FlaskForm):
    email= StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    age = IntegerField('Age')
    bio = StringField('Bio')
    password = PasswordField('Password', validators=[DataRequired()])
    password2= PasswordField('Re-type Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Invalid Username')
            raise ValidationError('Invalid Username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Invalid E-mail')
            raise ValidationError('Invalid E-mail')
