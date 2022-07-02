import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, request
from flask_restx import Api, Resource

# Logging mechanism
myLogger = logging.getLogger('main')

log_filename = os.path.join("log", "app.log")
os.makedirs(os.path.dirname(log_filename), exist_ok=True)
myHandler = RotatingFileHandler(log_filename, mode='a', maxBytes=20000000, backupCount=5)

myHandler.setLevel(logging.INFO)
myHandler.setFormatter(logging.Formatter('(%(threadName)s) %(asctime)s %(message)s'))
myLogger.addHandler(myHandler)
myLogger.setLevel(logging.INFO)

PORT = 5666

flask_app = Flask(__name__)
app = Api(app=flask_app)
myLogger.info("Flask app started")

nameSpace = app.namespace('', description='Main APIs')


@nameSpace.route('/helloWorld')
class Hello(Resource):
    def get(self):
        return 'Hello, World!'


@nameSpace.route('/postSomething')
@nameSpace.param(name="something", description="Something")
class Something(Resource):
    def post(self):
        something = request.args['something']
        return f"Here's something : {something}", 200


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=PORT)
