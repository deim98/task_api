from flask import Blueprint, jsonify, request, abort
from marshmallow import ValidationError
from user_service.schemas.user_schema import user_schema, users_schema
from flask_restx import Api, Resource, fields, Namespace
import requests
import uuid

api = Namespace("users", description="User related operations")

# Sample in-memory storage for users
users = []
user_id_counter = 1

# Define the user model for documentation purposes using Flask-RESTX's `fields`
user_model = api.model('User', {
    'id': fields.Integer(required=True, description='The user identifier'),
    'username': fields.String(required=True, description='The username of the user'),
    'email': fields.String(required=True, description='The email of the user')
})

# UserList class to handle GET and POST requests for users
@api.route("/")
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        # Retrieve all users
        return users

    @api.expect(user_model)
    def post(self):
        # Create a new user
        global user_id_counter
        try:
            data = request.get_json()
            validated_data = user_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_user = validated_data
        new_user["id"] = user_id_counter
        users.append(new_user)
        user_id_counter += 1
        return jsonify(new_user), 201

# User class to handle GET requests for a single user
@api.route("/<int:id>")
class User(Resource):
    @api.marshal_with(user_model)
    def get(self, id):
        # Retrieve a user by ID
        user = next((user for user in users if user["id"] == id), None)
        if not user:
            abort(404, description="User not found")
        return user

# UserTasks class to handle GET requests for tasks assigned to a user
@api.route("/<int:id>/tasks")
class UserTasks(Resource):
    def get(self, id):
        # Retrieve tasks assigned to a specific user (mocked)
        user = next((user for user in users if user["id"] == id), None)
        if not user:
            abort(404, description="User not found")

        # Mocked response simulating assigned tasks; replace with actual task-service API call if needed
        tasks = [
            {"id": 1, "title": "Task 1 for user", "description": "Mocked task 1", "completed": False},
            {"id": 2, "title": "Task 2 for user", "description": "Mocked task 2", "completed": True},
        ]
        return jsonify(tasks), 200
