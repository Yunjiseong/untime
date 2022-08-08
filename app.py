import werkzeug
from flask import Flask, request, g
from flask_bcrypt import Bcrypt
from blueprints.v1_0 import blueprint as api_v1_0
from config.db_config import DataConfig as cf
from sqlalchemy import pool
import pymysql as pm

app = Flask(__name__, static_folder='static', template_folder='templates')

# @app.before_first_request: 웹 기동 후 처음 들어오는 http 요청에서만 실행


@app.before_request
def before_request():
    app.logger.debug(request)
    g.db = app.db_master_pool.connect()


@app.after_request
def after_request(response):
    app.logger.debug(response)

    return response


app.register_blueprint(api_v1_0)

db_conf, db_kw_conf = cf.untime_db_config(False)
app.db_master_pool = pool.QueuePool(lambda: pm.connect(**db_conf), **db_kw_conf)

app.config['SECRET_KEY'] = 'untime is a perfect app'
app.config['BCRYPT_LEVEL'] = 10
bcrypt = Bcrypt(app)

if __name__ == '__main__':
    app.run(use_reloader=True)