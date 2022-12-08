from flask import Blueprint, request, redirect
from .. import dbModels

recipe_ingr_bp = Blueprint('recipe_ingr', __name__, url_prefix='/recipe_ingr')

@recipe_ingr_bp.route('/', methods=['GET', 'POST'])
def recipe_ingr():
    return