from flask import Flask


app = Flask(__name__)
pets = {
    "cats": [
        {
            "age": 1,
            "breed": "Tabby",
            "description": "Snowflake is a playful kitten who loves roaming the house and exploring.",
            "name": "Snowflake",
            "url": "https://content.codecademy.com/programs/flask/introduction-to-flask/cat-snowflake.jpeg",
        }
    ],
    "dogs": [
        {
            "age": 2,
            "breed": "Dalmatian",
            "description": "Spot is an energetic puppy who seeks fun and adventure!",
            "name": "Spot",
            "url": "https://content.codecademy.com/programs/flask/introduction-to-flask/dog-spot.jpeg",
        },
        {
            "age": 4,
            "breed": "Border Collie",
            "description": "Eager and curious, Shadow enjoys company and can always be found tagging along at your heels!",
            "name": "Shadow",
            "url": "https://content.codecademy.com/programs/flask/introduction-to-flask/dog-shadow.jpeg",
        },
    ],
    "rabbits": [
        {
            "age": 4,
            "breed": "Mini Rex",
            "description": "Easter is a sweet, gentle rabbit who likes spending most of the day sleeping.",
            "name": "Easter",
            "url": "https://content.codecademy.com/programs/flask/introduction-to-flask/rabbit-easter.jpeg",
        }
    ],
}


# @app.route("/")
# def index():
#     return f"""
#     <h1>Hello baby</h1>
#     <ul>
#     <li><a href="/animals/dogs">{pets["dogs"][0]["name"]}</a></li>
#     <li><a href="/pet_detail">{pets["cats"][0]["name"]}</a></li>
#     <li><a href="/animals/rabbits">{pets["rabbits"][0]["name"]}</a></li>
#     </ul>
#         """


@app.route("/animals")
def main_page():
    return f"""
     <h1>List animals: </h1>
    <ul>
     <li><a href="/animals/dogs">{pets["dogs"][0]["name"]}</a></li>
    <li><a href="/pet_detail">{pets["cats"][0]["name"]}</a></li>
    <li><a href="/animals/rabbits">{pets["rabbits"][0]["name"]}</a></li>
   </ul>
    """


@app.route("/animals/<animal_type>")
def pet_list(animal_type):
    if animal_type in pets.keys():
        name = pets[animal_type][0]["name"]
        return f"""
        <h1>{animal_type}</h1>
        <ul>
            <li><a href="/animals/{animal_type}/{name}">{name}</a></li>
        </ul>
        """
    return f"""
        <p>We dont have such animals, but we have: </p>
        <ul>
            <li><a href="/animals/rabbits">Rabbits</a></li>
            <li><a href="/animals/cats">Cats</a></li>
            <li><a href="/animals/dogs">Dogs</a></li>
        </ul>
        """


@app.route("/animals/<animal_type>/<animal_name>")
def pet_details(animal_type, animal_name):
    if (animal_type in pets.keys()) and (animal_name is not None):
        return f"""
        <p>Name: {animal_name}</p>
        <p>Age: {pets[animal_type][0]["age"]}</p>
        <p>Breed: {pets[animal_type][0]["breed"]}</p>
        <p>Description: {pets[animal_type][0]["description"]}</p>
        """
    return f"Mistake"