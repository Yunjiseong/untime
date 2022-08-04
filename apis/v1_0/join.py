import pymysql as pm
import logging
import werkzeug
from flask import request, g
from flask_restplus import Namespace, fields, Resource, reqparse
from datetime import datetime

logger = logging.getLogger()
ns = Namespace('join', 'User Join api')

# args list
join_parser = reqparse.RequestParser()

# User 데이터 모델
model_join = ns.model('user_join', {
    'unique_num': fields.String(required=True, description='초대용 고유키', example='0183'),
    'name': fields.String(required=True, description='유저 별칭', example='곱단이'),
    'pw': fields.String(required=True, description='유저 비밀번호', example=''),
    'phone': fields.String(required=True, description='유저 폰번호', example='0101234567'),
    'upjang': fields.String(required=False, description='업장 이름', example='밤사'),
    'type': fields.String(required=True, description='구분(업장, 매댐, 꿀벌)', example='꿀벌'),
    'license': fields.String(required=False, description='업장, 매댐용 라이센스', example='')
})


@ns.route('/')
@ns.doc(response={200: 'Success', 300: 'Redirected', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
@ns.expect(model_join)
class JoinUser(Resource):
    def post(self, data):
        '''
        회원가입
        :return:
        '''

        # conn = g.db
        # cur = conn.cursor()

        try:
            args = request.json
            print('args:', args)

            sql = f"""
                    INSERT INTO untime.tb_user
                    VALUES({args['unique_key']}, {args['name']}, {args['pw']}, {args['phone']}, {args['upjang']}, {args['type']}, {args['license']})
                """
        except Exception as e:
            print('join 에러 발생!', e)

        return {'result': 'success', 'data': args}

