from flask import Blueprint, request, redirect
from .. import dbModels

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route('/', methods=['GET', 'POST'])
def recipes():
    return