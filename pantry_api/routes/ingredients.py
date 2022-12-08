from flask import Blueprint, request, redirect
from .. import dbModels

ingr_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients')

@ingr_bp.route('/', methods=['GET', 'POST'])
def ingredients():
    if request.method == 'POST':
        new_ingr = dbModels.Ingredient(
            ingredient_name = request.form['ingredient_name']
        )

        dbModels.db.session.add(new_ingr)
        dbModels.db.session.commit()
        return f'new ingredient: {new_ingr.ingredient_name} added'
    found_ingr = dbModels.Ingredient.query.all()
    ingr_dict = {'ingredients':[]}
    for ingr in found_ingr:
        ingr_dict['ingredients'].append({
            'ingredient_name':ingr.ingredient_name
        })
    return ingr_dict
    