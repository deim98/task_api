from flask import Blueprint, jsonify, request, abort
from marshmallow import ValidationError
from task_service.schemas.task_schema import task_schema, tasks_schema
from flask_restx import Api, Resource, fields, Namespace


api = Namespace("tasks", description="Task related operations")

#Sample in-memory storage for tasks
tasks = []
task_id_counter = 1

# Define the task model for documentation purposes using Flask-RESTX's `fields`
task_model = api.model('Task', {
    'id': fields.Integer(required=True, description='The task identifier'),
    'title': fields.String(required=True, description='The task title'),
    'description': fields.String(required=True, description='The task description'),
    'completed': fields.Boolean(required=True, description='Task completion status')
})

# TaskList class to handle GET and POST requests for tasks
@api.route("/")
class TaskList(Resource):
    @api.marshal_list_with(task_model)
    def get(self):
        # Retrieve all tasks
        return tasks

    @api.expect(task_model)
    def post(self):
        # Create a new task
        global task_id_counter
        try:
            data = request.get_json()
            validated_data = task_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        # Add id and store the task
        new_task = validated_data
        new_task["id"] = task_id_counter
        tasks.append(new_task)
        task_id_counter += 1
        return jsonify(new_task), 201

# Task class to handle GET, PATCH requests for a single task
@api.route("/<int:id>")
class Task(Resource):
    @api.marshal_with(task_model)
    def get(self, id):
        # Retrieve a task by ID
        task = next((task for task in tasks if task["id"] == id), None)
        if not task:
            abort(404, description="Task not found")
        return task

    @api.expect(task_model)
    def patch(self, id):
        # Update a specific task
        task = next((task for task in tasks if task["id"] == id), None)
        if not task:
            abort(404, description="Task not found")

        data = request.get_json()
        try:
            validated_data = task_schema.load(data, partial=True)
        except ValidationError as err:
            return jsonify(err.messages), 400

        # Update only the fields provided in the request
        task.update(validated_data)
        return jsonify(task), 200