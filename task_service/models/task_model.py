from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()

class Task:
    @staticmethod
    def init_app(app):
        mongo.init_app(app)

    @staticmethod
    def create_task(data):
        return mongo.db.tasks.insert_one(data).inserted_id

    @staticmethod
    def get_tasks():
        return list(mongo.db.tasks.find())

    @staticmethod
    def get_task(task_id):
        return mongo.db.tasks.find_one({"_id": ObjectId(task_id)})

    @staticmethod
    def update_task(task_id, data):
        return mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": data})