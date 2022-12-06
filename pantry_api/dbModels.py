from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)



class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String)


# class User_Ingredient(db.Model):
#     __tablename__ = 'user_ingredients'


# class Pantry_Item(db.Model):
#     __tablename__ = 'pantry_items'


# class Grocery_List_Item(db.Model):
#     __tablename__ = 'grocery_list_items'


# class Recipe(db.Model):
#     __tablename__ = 'recipes'


# class Recipe_Ingredient(db.Model):
#     __tablename__ = 'recipe_ingredients'

# class Meal_Plan(db.Model):
#     __tablename__ = 'meal_plans'