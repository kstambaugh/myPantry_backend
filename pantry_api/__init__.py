#config
import os
from dotenv import load_dotenv
from flask import Flask, redirect, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS



#factory
def create_app():

    app = Flask(__name__)
    CORS(app)

    #config
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI']= os.getenv("DATABASE_URI")
    app.config['SQLALCHMEY_TRACK_MODIFICATIONS']=False
    
   
    
    from . import dbModels
    dbModels.db.init_app(app)
    migrate = Migrate(app, dbModels.db)


    @app.route("/")
    def index():
            return 'hello'

    from .routes import users
    app.register_blueprint(users.user_bp)

    from .routes import ingredients
    app.register_blueprint(ingredients.ingr_bp)

      

    return app