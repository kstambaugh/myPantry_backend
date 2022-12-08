from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)

    user_ingredients = db.relationship('User_Ingredient', backref='users')
    grocery_list_items = db.relationship('Grocery_List_Item', backref='users')
    user_recipes = db.relationship('Recipe', backref='users')

    def __init__(self, name, password ):
        self.name=name
        self.password=password

    def __repr__(self):
        return f'<User {self.name}>'



class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String)

    user_ingredients = db.relationship('User_Ingredient', backref='ingredients')
    grocery_list_items = db.relationship('Grocery_List_Item', backref='ingredients')
    recipe_ingredients = db.relationship('Recipe_Ingredient', backref='ingredients')

    def __init__(self, ingredient_name):
        self.ingredient_name=ingredient_name

    def __repr__(self):
        return f'<Ingredient {self.ingredient_name}>'


class User_Ingredient(db.Model):
    __tablename__ = 'user_ingredients'

    user_ingredient_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))

    pantry_items = db.relationship('Pantry_Item', backref='user_ingredients')

    def __init__(self, user_id, ingredient_id):
        self.user_id=user_id
        self.ingredient_id=ingredient_id

    def __repr__(self):
        return f'<User_Ingredient {self.user_id, self.ingredient_id}>'


class Pantry_Item(db.Model):
    __tablename__ = 'pantry_items'

    pantry_item_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    unit_of_measure = db.Column(db.String(10))
    user_ingredient_id = db.Column(db.Integer, db.ForeignKey('user_ingredients.user_ingredient_id'))

    def __init__(self, quantity, unit_of_measure, user_ingredient_id):
        self.quantity=quantity
        self.unit_of_measure=unit_of_measure
        self.user_ingredient_id = user_ingredient_id

    def __repr__(self):
        return f"<Pantry_Item {self.user_ingredient_id, self.quantity, self.unit_of_measure}>"


class Grocery_List_Item(db.Model):
    __tablename__ = 'grocery_list_items'

    grocery_item_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    unit_of_measure = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))

    def __init__(self, ingredient_id, user_id, quantity, unit_of_measure):
        self.ingredient_id=ingredient_id
        self.user_id=user_id
        self.quantity=quantity
        self.unit_of_measure=unit_of_measure

    def __repr__(self):
        return f"<Grocery_List_Item {self.ingredient_id, self.quantity, self.unit_of_measure, self.user_id, self.ingredient_id}>"

class Recipe(db.Model):
    __tablename__ = 'recipes'

    user_recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(250))
    method_instructions = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    recipe_ingredients = db.relationship('Recipe_Ingredient', backref='recipes')
    mealplans = db.relationship('Meal_Plan', backref='recipes')

    def __init__(self, recipe_name, method_instructions, user_id):
        self.recipe_name=recipe_name
        self.method_instructions = method_instructions
        self.user_id = user_id

    def __repr__(self):
        return f"<Recipe {self.recipe_name, self.method_instructions, self.user_id}>"
        
    

class Recipe_Ingredient(db.Model):
    __tablename__ = 'recipe_ingredients'

    recipe_ingredient_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    unit_of_measure = db.Column(db.String(10))
    user_recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.user_recipe_id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))

    def __init__(self, quanity, unit_of_measure, user_recipe_id, ingredient_id):
        self.quantity = quanity
        self.unit_of_measure = unit_of_measure
        self.user_recipe_id = user_recipe_id
        self.ingredient_id = ingredient_id

    def __repr__(self):
        return f"<Recipe_Ingredient {self.ingredient_id, self.quantity, self.unit_of_measure, self.user_recipe_id}>"
        


class Meal_Plan(db.Model):
    __tablename__ = 'meal_plans'

    meal_plan_id = db.Column(db.Integer, primary_key=True)
    user_recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.user_recipe_id'))

    def __init__(self, user_recipe_id):
        self.user_recipe_id = user_recipe_id

    def __repr__(self):
        return f"<Meal_Plan {self.user_recipe_id}>"
