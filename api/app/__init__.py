from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)
from views import posts, hello