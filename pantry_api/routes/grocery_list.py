from flask import Blueprint, request, redirect
from .. import dbModels

grocery_bp = Blueprint('grocery', __name__, url_prefix='/grocery')

@grocery_bp.route('/', methods=['GET', 'POST'])
def grocery():
    return