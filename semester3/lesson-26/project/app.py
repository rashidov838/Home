import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Путь создает
basedir = os.path.abspath(os.path.dirname(__file__))
# Подключаем базу данных
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" \
    + os.path.join(basedir, "myDb.db")
# уведомление уберает
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Recipe(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    recipes=db.Column(db.String(80),index=True, unique=False )
    types=db.Column(db.String(80),index=True, unique=False )
    descriptions=db.Column(db.String(80),index=True, unique=False )
    new_ingredients=db.Column(db.TextArea,index=True, unique=False )
    new_instructions=db.Column(db.TextArea,index=True, unique=False )
    comment = db.relationship(
        "Comment",
        backref="recipe",
        lazy="dynamic",
        cascade="all, delete, delete-orphan",
    )
    def __repr__(self):
        return "{} in:  {}, {}".format(self.id, self.recipes, self.types)


class Comment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    body=db.Column(db.String(100))
    timestamp = db.Column(db.DateTime)
    recipe_id=db.Column(db.Integer, db.ForeignKey('recipe.id'))
    def __repr__(self):
        return f"Comment('{self.body}', '{self.timestamp}')"
