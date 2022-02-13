import flask_restful
import responses
import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = flask_restful.Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class email(Resource):
    def post(self):
        return {'message': "posted successfully"}, 200


    pass

api.add_resource(email, '/email')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8001")

