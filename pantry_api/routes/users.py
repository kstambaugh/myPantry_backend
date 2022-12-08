from flask import Blueprint, request, redirect
from .. import dbModels

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET','POST'])
def users():
    if request.method == 'POST':
        new_user = dbModels.User(
            name = request.form['name'],
            password = request.form['password']
        )

        dbModels.db.session.add(new_user)
        dbModels.db.session.commit()
        return redirect('/users')

    found_Users = dbModels.User.query.all()
    user_dict = {'users': []}
    for user in found_Users:
        user_dict['users'].append({
            'name':user.name,
            'password': user.password
        })
    return user_dict
