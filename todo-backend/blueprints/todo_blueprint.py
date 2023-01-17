from flask import Blueprint, jsonify, request, abort
from daos.todo_dao import TodoDao
from serialisers.todo_serialiser import TodoSerialiser
import json
import datetime
import logging

logger = logging.getLogger(__name__)


def create_todo_blueprint(blueprint_name: str, url_prefix: str):
    todo_blueprint = Blueprint(blueprint_name, __name__, url_prefix=url_prefix)

    @todo_blueprint.route('/', methods=['GET'])
    def get_todos():
        todos = TodoDao.get_todos()
        return jsonify([TodoSerialiser.serialise(todo) for todo in todos])

    @todo_blueprint.route('/', methods=['POST'])
    def create_todo():
        data = json.loads(request.data)
        name = data.get('name')
        description = data.get('description')
        deadline = data.get('deadline')
        if deadline:
            deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d')
        completed = data.get('completed')
        todo = TodoDao.create_todo(
            name=name,
            description=description,
            deadline=deadline,
            completed=completed
        )
        return jsonify(TodoSerialiser.serialise(todo))

    @todo_blueprint.route('/<id>', methods=['GET'])
    def get_todo_by_id(id):
        todo = TodoDao.get_todo_by_id(id)
        if not todo:
            abort(404)
        return jsonify(TodoSerialiser.serialise(todo))

    @todo_blueprint.route('/<id>', methods=['DELETE'])
    def delete_todo_by_id(id):
        todo = TodoDao.get_todo_by_id(id)
        if not todo:
            abort(404)
        TodoDao.delete_todo_by_id(id)
        return jsonify(TodoSerialiser.serialise(todo))

    return todo_blueprint
