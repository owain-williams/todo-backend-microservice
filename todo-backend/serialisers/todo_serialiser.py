class TodoSerialiser:
    @staticmethod
    def serialise(todo):
        return {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'deadline': todo.deadline,
            'created': todo.created,
            'completed': todo.completed
        }