#config
from flask import Flask, redirect
from flask_migrate import Migrate


#factory
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost:5432/mypantry_app'
    app.config['SQLALCHMEY_TRACK_MODIFICATIONS']=False

    from . import dbModels
    dbModels.db.init_app(app)
    migrate = Migrate(app, dbModels.db)


    @app.route("/")
    def index():
        return "hello world"

    return app