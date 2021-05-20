from flask import Flask, jsonify
import pandas as pd
import json
from flask import request
import os
import os.path
from os import path
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config["SQLALCHEMY_DATABSE_URI"] = "sqlite:///example.db"
# data = pd.read_csv('../src/csvs/poke.csv')
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)


#     def __str__(self):
#         return f'{self.id} {self.content}'

# def todo_serializer(todo):
#     return {
#         'id': todo_id,
#         'content': todo_content
#     }
# # print(data)

@app.route("/team", methods=['POST'])
def team():
    # id sent over is "poke name"
    # JSON BODY: "turtwig", ""
    main_poke = request.json 
   
    if main_poke:
        from grab import team_builder
        team_builder(main_poke)
        return 'Created Team', 201
    return "No Starting Pokemon was Chosen"

@app.route("/pokemon", methods=['GET'])
def pokemon():

    with open('./team.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    return json.dumps(file_data)
    # {
    #     "pokemon": 
    # [
    #     {
    #         "pokemon_id" : "000",
    #         "pokemon_data" : {
    #             "name" : "Elise",
    #             "age" : 26,
    #             "birthday" : "03/10/1995"
    #         }
    #     },{
    #         "person_id" : "001",
    #         "person_data" : {
    #             "name" : "Christine",
    #             "age" : 26,
    #             "birthday" : "04/14/1995"
    #         }
    #     }
    # ]}
    # return jsonify([*map(todo_serializer, Todo.query.all())])
    # pokemon.pokemon_data.name 
if __name__ == '__main__':
    app.run(debug=True)


