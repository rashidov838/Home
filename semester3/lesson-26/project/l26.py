from flask import Flask, render_template, url_for, request, redirect
from helper import (recipes, types, descriptions, ingredients,
                    instructions, comments, add_ingredients, add_instructions)
from forms import RecipeForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"


# @app.route("/recipes")
@app.route("/", methods=["GET", "POST"])
def main_page():
    recipe_form = RecipeForm(csrf_enabled=False)
    # if request.method=="POST":
    # recipe_form.data["recipe"]
    # recipe_form.recipe.data
    if recipe_form.validate_on_submit():
        new_id = len(recipes)+1
        recipes[new_id] = recipe_form.recipe.data
        types[new_id] = recipe_form.recipe_type.data
        descriptions[new_id] = recipe_form.description.data
        new_ingredients = recipe_form.ingredients.data
        new_instructions = recipe_form.instructions.data
        add_ingredients(new_id, new_ingredients)
        add_instructions(new_id, new_instructions)
        comments[new_id] = []
        return redirect(url_for("recipe", id=new_id, recipes=recipes, types=types, descriptions=descriptions, ingredients=new_ingredients, instructions=new_instructions))

    return render_template("index.html", title="Homee", recipes=recipes, form=recipe_form)


@app.route("/recipe/<int:id>/", methods=["GET", "POST"])
def recipe(id):

    return f"Recipe with  # {id}: <br> Recipe: {recipes[id]}; <br> Types: {types[id]}; <br> Description: {descriptions[id]}; <br> New_ingredients:{ingredients[id][0]}; <br> New_instructions:{list(instructions[id].values())[0]}"


@app.route("/about")
def about():
    return render_template("about.html", title="About")
