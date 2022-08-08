import pymysql as pm
import logging
import werkzeug
from flask import request, g
from flask_restplus import Namespace, fields, Resource, reqparse
from datetime import datetime
from app import bcrypt

logger = logging.getLogger()
ns = Namespace('join', 'User Join api')

# args list
join_parser = reqparse.RequestParser()

# User 데이터 모델
model_join = ns.model('user_join', {
    'user_seq': fields.String(required=True, description='사용자 pk', example='183'),
    'name': fields.String(required=True, description='유저 별칭', example='곱단이'),
    'pw': fields.String(required=True, description='유저 비밀번호', example='asset7878!'),
    'pwCheck': fields.String(required=True, description='유저 비밀번호 확인', example='asset7878!'),
    'phone': fields.String(required=True, description='유저 폰번호', example='0101234567'),
    'upjang': fields.String(required=False, description='업장 이름', example='밤사'),
    'type': fields.String(required=True, description='구분(업장, 매댐, 꿀벌)', example='꿀벌'),
    'license': fields.String(required=False, description='업장, 매댐용 라이센스', example='Ksaekd12')
})


@ns.route('')
@ns.doc(response={200: 'Success', 300: 'Redirected', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
@ns.expect(model_join)
class JoinUser(Resource):
    def post(self):
        '''
        회원가입
        :return:
        '''

        conn = g.db
        cur = conn.cursor()

        try:
            args = request.json
            print('args:', args)
            now = datetime.now().strftime("%Y%m%d")
            encrypt_pw = bcrypt.generate_password_hash(args['pw'])

            sql = f"""
                    INSERT INTO untime.tb_user
                    VALUES(NULL, {args['name']}, {encrypt_pw}, {args['phone']}, {args['upjang']}, 
                    {args['type']}, {args['license']}, {now})
                """
            cur.execute(sql)
            conn.commit()

            return {'result': 'success'}
        except Exception as e:
            print('join 에러 발생!', e)
            return {'result': 'fail', 'message': e}
        finally:
            conn.close()


@ns.route('/sms')
@ns.hide
@ns.doc(response={200: 'Success', 300: 'Redirected', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
class SendSMS(Resource):
    def post(self):
        '''
        SMS 인증
        :return:
        '''
        print()




