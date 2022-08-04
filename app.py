import werkzeug
from flask import Flask, request, g
from blueprints.v1_0 import blueprint as api_v1_0
from sqlalchemy import pool
import pymysql as pm

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.before_request
def before_request():
    app.logger.debug(request)


@app.after_request
def after_request(response):
    app.logger.debug(response)

    return response


app.register_blueprint(api_v1_0)

# db_conf, db_kw_conf =
# app.db_master_pool = pool.QueuePool(lambda: pm.connect(**db_conf), **db_kw_conf)

if __name__ == '__main__':
    app.run(use_reloader=True)