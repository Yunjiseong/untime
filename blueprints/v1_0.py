from flask_restplus import Api
from flask import Blueprint
from apis.v1_0.join import ns as join

authorization = {
    'Bearer Auth': {'type': 'apiKey', 'in': 'header', 'name': 'Authorization'},
}

blueprint = Blueprint('api_1_0', __name__, url_prefix='/v1.0')

api = Api = Api(
    blueprint,
    version='1.0',
    title='Untime Server',
    description='Untime 백엔드 서버',
    doc='/docs',
    security='Bearer Auth',
    authorizations=authorization
)

api.add_namespace(join)