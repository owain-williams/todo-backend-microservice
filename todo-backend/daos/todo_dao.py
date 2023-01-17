from database import db
from typing import List
from models.todo import Todo
import uuid


class TodoDao:
    @staticmethod
    def create_todo(name, description='', deadline=None, completed=False):
        todo = Todo(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            deadline=deadline,
            completed=completed
        )
        db.session.add(todo)
        db.session.commit()
        return todo

    @staticmethod
    def get_todos() -> List[Todo]:
        return Todo.query.all()

    @staticmethod
    def get_todo_by_id(id) -> Todo:
        return Todo.query.filter_by(id=id).first()

    @staticmethod
    def delete_todo_by_id(id):
        todo = Todo.query.filter_by(id=id).first()
        db.session.delete(todo)
        db.session.commit()
