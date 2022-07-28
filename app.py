import werkzeug
from flask import Flask, request, g
from blueprints.v1_0 import blueprint as api_v1_0

app = Flask(__name__, static_folder='static', template_folder='templates')