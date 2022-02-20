import flask_restful
from flask import Flask
from flask_restful import Resource, Api, reqparse
import re
import random
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = flask_restful.Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def email_check(email):
    regex = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    if re.search(regex, email):
        return True
    else:
        return False

def check_verify(verification_code, submit_verification):
    if (len(submit_verification) == 6) and submit_verification.isdigit():
        if verification_code == int(submit_verification):
            return True
        else:
            return False
    else:
        return False


class email(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, help="This is not a valid input. please enter an email address.")
        content = str(parser.parse_args())
        #check if input is a valid email address
        if email_check(content):
            if "@jazzsucks.ca" in content:
                # generate verification code
                verification_code = random.randint(100000, 999999)

                return "verification code sent.", 200

            else:
                return "Please use a '@jazzsucks.ca email address.", 400
        else:
            return "This is not a valid input. please enter an email address.", 400

class verify(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('submit-verification', type=int, required=True, help="this is not a valid verification code.")



api.add_resource(email, '/email')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8001")

