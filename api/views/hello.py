from flask_restful import Resource
from api import api

@api.resource("/")
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        pass