from flask import Flask, jsonify
from database import db
from blueprints.todo_blueprint import create_todo_blueprint
import logging

logger = logging.getLogger(__name__)


def create_app(db_uri: str) -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(create_todo_blueprint('todo', '/todo'))

    return app


if __name__ == '__main__':
    app = create_app(db_uri='sqlite:///todo.db')
    app.run('0.0.0.0', port=8000, debug=True)
