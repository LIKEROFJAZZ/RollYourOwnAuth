import flask_restful
import responses
import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = flask_restful.Api(app)

class submitEmail(Resource):
    def get(self):
        return {'message': "no access"}, 401
    def post(self):
        return {'message': "posted successfully"}, 200


    pass

api.add_resource(submitEmail, '/submit-email')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8001")

