import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    MONGO_URI= os.getenv("MONGO_URI", "mongodb://mongo:27017/appdb")
    