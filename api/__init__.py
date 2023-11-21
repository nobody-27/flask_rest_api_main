from flask import Flask
from flask_restx import Api
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .config.config import config_dict

from .models.orders import Order
from .utils import db
from .models.user import User
from flask_migrate import Migrate



def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migret = Migrate(app,db)

    api = Api(app)
    api.add_namespace(order_namespace,path='/')
    api.add_namespace(auth_namespace,path='/auth')


    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'User':User,
            'Order':Order
        }

    return app



#export FLASK_APP = api/ when you have create api for linux (windows set FLASK_APP=api/ )
#pip install flask_restx is allow to make api in flask 