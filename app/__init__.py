from flask import Flask, Blueprint
from app.api import api
import os


basedir = os.path.dirname(os.path.abspath(__file__))
db_file = 'sqlite:///' + os.path.join(basedir, './db/born.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import tables  
from app.api.born import ns as born_api

blueprint = Blueprint('api', __name__, url_prefix='/api')

api.init_app(blueprint)
api.add_namespace(born_api)
app.register_blueprint(blueprint)
