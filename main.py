from flask import Flask
from flask_jwt_extended import JWTManager
from task_service.schemas.task_schema import task_schema, tasks_schema
from user_service.schemas.user_schema import user_schema, users_schema
from user_service.models.user_model import User
from task_service.models.task_model import Task
from flask_pymongo import PyMongo
from config import Config
from flask_restx import Api


app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

User.init_app(app)
Task.init_app(app)
jwt = JWTManager(app)


api = Api(app, version='1.0', title='Task and User API', description='A simple API for tasks and users', doc='/docs')

api.add_namespace(api, path='/tasks')
api.add_namespace(api, path='/users')

@app.route("/")
def home():
    return "Welcome to the Task and User Management API!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)