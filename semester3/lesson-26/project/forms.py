from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    recipe_categories=[
        ("Breakfast","Breakfast"),
        ("Lunch","Lunch"),
        ("Dinner","Dinner"),
    ]
    recipe=StringField('Recipe')
    recipe_type=RadioField("Type",choices=recipe_categories)
    description=StringField("Description")
    instructions=TextAreaField("Instruction")
    ingredients=TextAreaField("Ingredients")
    submit=SubmitField("Add recipe")