from flask import Blueprint, request, redirect
from .. import dbModels

meal_plan_bp = Blueprint('meal_plan', __name__, url_prefix='/meal_plan')

@meal_plan_bp.route('/', methods=['GET', 'POST'])
def meal_plan():
    return