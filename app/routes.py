from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/tasks')
def get_tasks():
    return jsonify({"message": "Hello from /tasks"})
