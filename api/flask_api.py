from flask import Flask
import flask_restful
from flask_restful import Resource

from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = flask_restful.Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class Email(Resource):
    def post(self):
        return {'message': "posted successfully"}, 200

    pass


api.add_resource(Email, '/email')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8001)
