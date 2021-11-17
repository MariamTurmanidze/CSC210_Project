from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
  employee_id = StringField('Employee ID', validators=[DataRequired()])
  password = PasswordField("Password", validators = [DataRequired()])
  remember_me = BooleanField("Keep me logged in")
  submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    employee_id = StringField('Employee_ID', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    ssn = StringField('SSN', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('address', validators=[DataRequired()])
    dep_name = StringField('Department Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_employeeid(self, employee_id):
        user = User.query.filter_by(employee_id=employee_id.data).first()
        if user:
            raise ValidationError('Please use a different employee_id.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Please use a different email address.')

