import pymysql as pm
import logging
import werkzeug
from flask import request, g
from flask_restplus import Namespace, fields, Resource, reqparse
from datetime import datetime
from app import bcrypt
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
    'pw': fields.String(required=True, description='pw', example='asset7878')
})


### login_service
def login_check(cur, ut_id, ut_pw):
    sql = "SELECT PW, USER_SEQ FROM untime.tb_user WHERE id=%s"
    # cur.execute(sql, ut_id)
    data = cur.fetchone()
    if data is None:
        return -1
    elif bcrypt.check_password_hash(ut_pw, data[0]):
        return data[1]

    return -1
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
        obj = {}
        try:
            args = request.json
            user_seq = login_check(cur, args['id'], args['pw'])
            if user_seq > -1:
                access_token = create_access_token(identity=user_seq, expires_delta=False)
                obj['access_token'] = access_token

                return {'result': 'success', 'data': obj}
            else:
                return {'result': 'fail'}
        except Exception as e:
            print('에러 발생!', e)
        finally:
            conn.close()



