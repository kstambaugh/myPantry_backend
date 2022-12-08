from flask import Blueprint, request, redirect
from .. import dbModels

pantry_bp = Blueprint('pantry', __name__, url_prefix='/pantry')

@pantry_bp.route('/', methods=['GET', 'POST'])
def pantry():
    return