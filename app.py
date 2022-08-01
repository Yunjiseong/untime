import werkzeug
from flask import Flask, request, g
from blueprints.v1_0 import blueprint as api_v1_0

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.before_request
def before_request():
    app.logger.debug(request)
    g.db = app


@app.after_request
def after_request(response):
    app.logger.debug(response)

    return response


app.register_blueprint(api_v1_0)

if __name__ == '__main__':
    app.run(use_reloader=True)