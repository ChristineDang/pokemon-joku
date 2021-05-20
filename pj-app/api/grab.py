import csv
import json
import pandas as pd
import random
import os
import os.path
from os import path
# import the data and fill the NAN with zero
data = pd.read_excel("../src/excel/turtwig.xlsx")
type_chart = pd.read_excel("../src/excel/pokemon_type.xlsx")
data = data.fillna(0)

global team_list
team_list = []

global weakness_list
weakness_list =[]

global strength_list
strength_list = []


team_examples = pd.read_excel("../src/excel/turtwig.xlsx")


def team_builder(x):
    team_list = []
    team_members = { "pokemon": []}
    team_list.append(x)
    # data["name"]
    # i.e Garadose => garadose
    grab_chosen_poke_name = data[data["Name"].str.lower() == team_list[0]]
    # grab_chosen_poke_name[colname][first item].lower case it
    # i.e. Garadose Type = Water => water
    grab_chosen_poke_type = grab_chosen_poke_name["Type 1"][0].lower()
    # type_chart[type_chart[Attacking Type] == water]
    # type_chart[water]
    type_chart_grab_1 = type_chart[type_chart["Attacking Type"] == grab_chosen_poke_type].drop(columns="Attacking Type")
    # type_chart[water].columns.to_list() => ["Normal", "Fighting",..."Fire"]
    type_column_names = type_chart_grab_1.columns.to_list()
    # i is index
    for i in type_column_names:
        if type_chart_grab_1[i].values == 0.5:
            weakness_list.append(i)
    # weakness_list length = < 5
    if len(weakness_list) > 5:
        diff = len(weakness_list) - 5
        for i in range(diff):
            weakness_list.pop(random.randrange(len(weakness_list)))
            print(len(weakness_list))
    else: pass
    # weakness_list = ['water','grass','dragon']
    print(weakness_list)
    # type_grab_2 = type_chart[type_chart["Attacking Type"] == water]
    # type_grab_2 = 'water' row?
    type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[0]]
    # i.e fire
    # grab cols where value = 0.5
    for i in type_column_names: # water_col
        if type_grab_2[i].values == 0.5:
            strength_list.append(i)
            # Steel appended i = 9
            # Fire appended i = 10
            # water appended i = 11
            # ice appended i = 15
    # strength_list = [steel, fire, water, ice]
    random_type = random.choice(strength_list)
    # data["fire"]
    poke_from_strength = data[data["Type 1"].str.lower() == random_type]
    # chosen_poke_type = random(Name_Col (fire) .to_list() => ['Rapidash',ponyta, charm]) => Rapidash
    print(len(poke_from_strength))
    print("0: " + poke_from_strength["Name"])
    chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
    team_list.append(chosen_type_poke)
    # team_list.append = ['Rapidash']

    # looking at grass pokemon
    type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[1]]
    for i in type_column_names:
        if type_grab_2[i].values == 0.5:
            strength_list.append(i)

    random_type = random.choice(strength_list)
    poke_from_strength = data[data["Type 1"].str.lower() == random_type]
    print("Strength: " + random_type)
    print(len(poke_from_strength)) # 0
    print("1: " + poke_from_strength["Name"])
    chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
    team_list.append(chosen_type_poke)
    # append turtwig
    # team_list = [Rapidash, Turtwig]
    type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[2]]
    print("weakness: " + weakness_list[2])
    for i in type_column_names:
        if type_grab_2[i].values == 0.5:
            strength_list.append(i)

    random_type = random.choice(strength_list)
    poke_from_strength = data[data["Type 1"].str.lower() == random_type]
    print(len(poke_from_strength))
    print("2: " + poke_from_strength["Name"])
    chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
    team_list.append(chosen_type_poke)
    # append Charazard
    # team_list = [Rapidash, Turtwig, Charazard]

    type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[3]]
    for i in type_column_names:
        if type_grab_2[i].values == 0.5:
            strength_list.append(i)

    random_type = random.choice(strength_list)
    poke_from_strength = data[data["Type 1"].str.lower() == random_type]
    print(len(poke_from_strength))
    print("3: " + poke_from_strength["Name"])
    chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
    team_list.append(chosen_type_poke)

    type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[4]]
    for i in type_column_names:
        if type_grab_2[i].values == 0.5:
            strength_list.append(i)

    random_type = random.choice(strength_list)
    poke_from_strength = data[data["Type 1"].str.lower() == random_type]
    print(len(poke_from_strength))
    print("4: " + poke_from_strength["Name"])
    chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
    team_list.append(chosen_type_poke)

    print(team_list)

    # def fill_teamdata():
    #     for i in team_list:
    #         print(i)
    #         poke = {}
    #         poke["name"] = team_list[i]
    #         add_poke(poke)
    if path.exists("./team.json"):
        os.remove("./team.json")
        print("deleted team")
    with open('./team.json', 'w') as jsonfile:

        for member in team_list:
            print(member)
            names = {}
            names["name"] = member
            team_members["pokemon"].append(names)
        json.dump(team_members, jsonfile)
            # And then we write a final newline to the end of the file 
            # (this is just a best practice)
        jsonfile.write('\n')
# team_builder("turtwig") 
# make the team_list => json
# api read that file
# manipulate on frontend

# print(team_builder("turtwig"))
