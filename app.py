import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, request
from flask_restx import Api, Resource


# Logging mechanism
myLogger = logging.getLogger('main')

log_filename = os.path.join("log","app.log")
os.makedirs(os.path.dirname(log_filename), exist_ok=True)
myHandler = RotatingFileHandler(log_filename, mode='a', maxBytes=20000000, backupCount=5)

myHandler.setLevel(logging.INFO)
myHandler.setFormatter(logging.Formatter('(%(threadName)s) %(asctime)s %(message)s'))
myLogger.addHandler(myHandler)
myLogger.setLevel(logging.INFO)

flask_app = Flask(__name__)
app = Api(app=flask_app)
myLogger.info("Flask app started")

nameSpace = app.namespace('', description='Main APIs')


@nameSpace.route('/hello')
class Hello(Resource):
    def get(self):
        return 'Hello, World!'

@nameSpace.route('/_setTargetImmunity')
@nameSpace.param(name="targetImmunity",description="Immunity you want to reach")
class SetTargetImmunity(Resource):
    def post(self):
        targetImmunity = request.args['targetImmunity']
        return f"Your target immunity has been set to {targetImmunity}", 200

@nameSpace.route('/_setVRFLevels')
@nameSpace.param(name="VRF1Level",description="VRF 1 Level")
@nameSpace.param(name="VRF1Level",description="VRF 2 Level")
@nameSpace.param(name="VRF3Level",description="VRF 3 Level")
@nameSpace.param(name="VRF4Level",description="VRF 4 Level")
class SetVRFLevels(Resource):
    def post(self):
        VRF1Level = request.args['VRF1Level']
        VRF2Level = request.args['VRF2Level']
        VRF3Level = request.args['VRF3Level']
        VRF4Level = request.args['VRF4Level']
        return f"Levels set to [{VRF1Level}, {VRF2Level}, {VRF3Level}, {VRF4Level}]", 200

@nameSpace.route('/giveMeMyAnswer')
class GiveMeMyAnswer(Resource):
    def post(self):

        return "Ne ne", 200

@nameSpace.route('/current_mode')
class GetScheduledJobs(Resource):
    def get(self):
        return "TODO"

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5666)
