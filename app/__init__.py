import os
import optparse
from flask import Flask, request, jsonify

from flask_restful import Api, Resource
from werkzeug.exceptions import HTTPException

from flask_cors import CORS


from app.config import Config



api = Api()






from flaskext.mysql import MySQL

mysql = MySQL()
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(Config)
    
    app.config['MYSQL_DATABASE_USER'] = "KLx1BRaegX"
    app.config['MYSQL_DATABASE_PASSWORD'] = "E8QdTdUoG5"
    app.config['MYSQL_DATABASE_DB'] = "KLx1BRaegX"
    app.config['MYSQL_DATABASE_HOST'] = "remotemysql.com"
    mysql.init_app(app)
    
   
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.crud import Orders, Items
 
    api.add_resource(Orders, '/orders', endpoint='orders')

    api.add_resource(Items, '/items', endpoint="items")
    
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):

        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'authorization,content-type,x-auth-token,Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,get,post,delete,put')
        return response

    from app.errors.handlers import errors
    app.register_blueprint(errors)

    api.init_app(app)
   

    return app
