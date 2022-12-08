from flask import Blueprint, request, redirect
from .. import dbModels

user_ingr_db = Blueprint('user_ingredients', __name__, url_prefix='/user_ingredients')

user_ingr_db.route("/", methods=['GET', 'POST'])
def user_ingedients():
    return 