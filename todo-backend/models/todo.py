from database import db
import datetime


class Todo(db.Model):
    __tablename__ = 'todos'
    
    id = db.Column(db.string(36), primary_key=True, unique=True)
    name = db.Column(db.string(255), primary_key=True, nullable=False)
    description = db.Column(db.string(255), nullable=True)
    deadline = db.Column(db.DateTime, nullable=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    completed = db.Column(db.Boolean, nullable=False, default=False)