from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()

class User:
    @staticmethod
    def init_app(app):
        mongo.init_app(app)

    @staticmethod
    def create_user(data):
        return mongo.db.users.insert_one(data).inserted_id

    @staticmethod
    def get_users():
        return list(mongo.db.users.find())

    @staticmethod
    def get_user(user_id):
        return mongo.db.users.find_one({"_id": ObjectId(user_id)})