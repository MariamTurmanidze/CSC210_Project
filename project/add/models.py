from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
  employee_id = db.Column(db.Integer, index=True, unique=True, primary_key=True, nullable=False)
  lname = db.Column(db.String(60), index=False, nullable=False)
  fname = db.Column(db.String(60), index=False, nullable=False)
  ssn = db.Column(db.Integer, index=True, unique=True, nullable=False)
  email = db.Column(db.String(60), index=False, unique=True, nullable=False)
  address = db.Column(db.String(60), index=False, nullable=False)
  dep_name = db.Column(db.String(60), index=False, nullable=False)
  password = db.Column(db.String(60), index=False, nullable=False)

  def get_id(self):
    return (self.employee_id)

  def __repr__(self):
    return f"User('{self.employee_id}', '{self.email}')"

@login_manager.user_loader
def load_user(employee_id):
   return User.query.get(int(employee_id))  
  
