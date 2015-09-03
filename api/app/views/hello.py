from flask_restful import Resource
from app import api

@api.resource("/hello")
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        pass