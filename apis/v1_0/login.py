import pymysql as pm
import logging
import werkzeug
from flask import request, g
from flask_restplus import Namespace, fields, Resource, reqparse
from datetime import datetime
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)

logger = logging.getLogger()
ns = Namespace('login', 'User Login api')

# Login 데이터 모델
model_login = ns.model('user_login',{
    'id': fields.String(required=True, description='id', example='untime123'),
    'pw': fields.String(required=True, description='pw', example='asset7878!')
})

### login_service
def login_check(cur, ut_id, ut_pw):
    sql = "SELECT COUNT(*) FROM untime.tb_user WHERE id=%s AND pw=%s"
    cur.execute(sql, (ut_id, ut_pw))
    data = cur.fetchone()
    if data == '0':
        return False
    else:
        return True

###



@ns.route('/login')
@ns.doc(response={200: 'Success', 300: 'Redirected', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
@ns.expect(model_login)
class LoginUser(Resource):
    def post(self):
        '''
        로그인
        :return:
        '''
        conn = g.db
        cur = conn.cursor()

        try:
            args = request.json
            if login_check(cur, args['id'], args['pw']):
                access_token = create_access_token(identity=args['user_seq'], expires_delta=False)


        except Exception as e:







