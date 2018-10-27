from flask_restplus import Api

api = Api(version='1.0', title='Born-Service', description='Born-Service Code')
ns  = api.namespace('v1', 'born')
