import pandas as pd
import random
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

# import the data and fill the NAN with zero
data = pd.read_excel("../src/excel/pokemon_dp_list.xlsx")
type_chart = pd.read_excel("../src/excel/pokemon_type.xlsx")
data = data.fillna(0)

############### the pokemon selector ##################

# def pokemon_chooser():
    
#     global chosen_poke
#     chosen_poke = []
    
#     print("Choose your pokemon")
#     while True:
#         inp = input("chimchar, piplup or turtwig:  ")
#         if inp.lower() == "quit":
#             break
#         elif inp.lower() == "chimchar":
#             print("chimchar was chosen")
#             chosen_poke.append(inp)
#             break
#         elif inp.lower() == "piplup":
#             print("piplup was chosen")
#             chosen_poke.append(inp)
#             break
#         elif inp.lower() == "turtwig":
#             print("turtwig was chosen")
#             chosen_poke.append(inp)
#             break
#         else:
            # print("try again")

global team_list
team_list = []

global weakness_list
weakness_list =[]

global strength_list
strength_list = []

def pokemon_chooser(chosen_poke):
    team_list = []
    if chosen_poke == ["turtwig"]:
    
        team_examples = pd.read_excel("../src/excel/turtwig.xlsx")
        

        def team_builder(x):
            
            x = x[0]
            team_list.append(x)
            grab_chosen_poke_name = data[data["Name"].str.lower() == team_list[0]]
            grab_chosen_poke_type = grab_chosen_poke_name["Type 1"][0].lower()
            type_chart_grab_1 = type_chart[type_chart["Attacking Type"] == grab_chosen_poke_type].drop(columns="Attacking Type")
            type_column_names = type_chart_grab_1.columns.to_list()

            for i in type_column_names:
                if type_chart_grab_1[i].values == 0.5:
                    weakness_list.append(i)

            if len(weakness_list) > 5:
                diff = len(weakness_list) - 5
                for i in range(diff):
                    weakness_list.pop(random.randrange(len(weakness_list)))
            else: pass

            print(weakness_list)

            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[0]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)


            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[1]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)

            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[2]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            # print(chosen_type_poke)

            team_list.append(chosen_type_poke)

            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[3]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)

            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[4]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)

            print(team_list)

    elif chosen_poke == ["chimchar"]:
        
        team_examples = pd.read_excel("../src/excel/chimchar.xlsx")

        def team_builder(x):
            x = x[0]
            team_list.append(x)
            grab_chosen_poke_name = data[data["Name"].str.lower() == team_list[0]]
            grab_chosen_poke_type = grab_chosen_poke_name["Type 1"].values[0].lower()
            type_chart_grab_1 = type_chart[type_chart["Attacking Type"] == grab_chosen_poke_type]
            type_chart_grab_1 = type_chart_grab_1.drop(columns="Attacking Type")
            type_column_names = type_chart_grab_1.columns.to_list()
            for i in type_column_names:
                if type_chart_grab_1[i].values == 0.5:
                    weakness_list.append(i)

            print(weakness_list)

        #     if len(weakness_list) > 4:
        #         diff = len(chim_weakness_list) - 3
        #         for i in range(diff):
        #             chim_weakness_list.pop(random.randrange(len(chim_weakness_list)))
        #     else: pass

        #     print(chim_weakness_list)

            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[0]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)


            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[1]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)


            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[2]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)

            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[3]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)

            ############## random pokemon selected because there are only 4 weaknesses, therefore need another way to select a 5th
            role_list =[]

            poke_grab_attacker = data[data["Complete Attacker"] == "Yes"]
            poke_chosen_attacker = random.choice(poke_grab_attacker["Name"].to_list())
            role_list.append(poke_chosen_attacker)

            poke_grab_attacker = data[data["Complete Tank"] == "Yes"]
            poke_chosen_attacker = random.choice(poke_grab_attacker["Name"].to_list())
            role_list.append(poke_chosen_attacker)

            poke_grab_attacker = data[data["Support"] == "Yes"]
            poke_chosen_attacker = random.choice(poke_grab_attacker["Name"].to_list())
            role_list.append(poke_chosen_attacker)

            poke_grab_attacker = data[data["All Rounder"] == "Yes"]
            poke_chosen_attacker = random.choice(poke_grab_attacker["Name"].to_list())
            role_list.append(poke_chosen_attacker)

            top_role_pick = random.choice(role_list)
            team_list.append(top_role_pick)

            print(team_list)
            
            
    elif chosen_poke == ["piplup"]:
        
        team_examples = pd.read_excel("../src/excel/piplup.xlsx")

        def team_builder(x):
            x = x[0]
            team_list.append(x)
            grab_chosen_poke_name = data[data["Name"].str.lower() == team_list[0]]
            grab_chosen_poke_type = grab_chosen_poke_name["Type 1"].values[0].lower()
            type_chart_grab_1 = type_chart[type_chart["Attacking Type"] == grab_chosen_poke_type]
            type_chart_grab_1 = type_chart_grab_1.drop(columns="Attacking Type")
            type_column_names = type_chart_grab_1.columns.to_list()
            for i in type_column_names:
                if type_chart_grab_1[i].values == 0.5:
                    weakness_list.append(i)

            weakness_list.append('electric')
            print(weakness_list)

    #         if len(weakness_list) > 3:
    #             diff = len(weakness_list) - 3
    #             for i in range(diff):
    #                 weakness_list.pop(random.randrange(len(weakness_list)))
    #         else: pass

            print(weakness_list)

            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[0]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)


            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[1]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)


            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[2]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)
            
            type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[3]]
            for i in type_column_names:
                if type_grab_2[i].values == 0.5:
                    strength_list.append(i)

            random_type = random.choice(strength_list)
            poke_from_strength = data[data["Type 1"].str.lower() == random_type]
            chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
            team_list.append(chosen_type_poke)

            ############## random pokemon selected because there are only 4 weaknesses, therefore need another way to select a 5th
            role_list =[]

            poke_grab_attacker = data[data["Complete Attacker"] == "Yes"]
            poke_chosen_attacker = random.choice(poke_grab_attacker["Name"].to_list())
            role_list.append(poke_chosen_attacker)

            poke_grab_attacker = data[data["Complete Tank"] == "Yes"]
            poke_chosen_attacker = random.choice(poke_grab_attacker["Name"].to_list())
            role_list.append(poke_chosen_attacker)

            poke_grab_attacker = data[data["Support"] == "Yes"]
            poke_chosen_attacker = random.choice(poke_grab_attacker["Name"].to_list())
            role_list.append(poke_chosen_attacker)

            poke_grab_attacker = data[data["All Rounder"] == "Yes"]
            poke_chosen_attacker = random.choice(poke_grab_attacker["Name"].to_list())
            role_list.append(poke_chosen_attacker)

            top_role_pick = random.choice(role_list)
            team_list.append(top_role_pick)

            print(team_list)
        
#############################################################

    team_builder(chosen_poke)

############################################################

    type_list = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy', 'none']
    number_range = list(range(19))
    type_dict = dict(zip(type_list, number_range))
    ability_dict = {"Levitate": 1, "Sand Stream":2, "Sand Veil":3, "Dry Skin":4, "Heat Proof":5} 
    yes_no_dict = {"Yes": 2, "No":1}
    type_list = list(type_chart.columns)
    type_list.remove('Attacking Type')
    type_list.append("none")
    number_range = list(range(19))
    type_dict = dict(zip(type_list, number_range))
    ability_dict = {"Levitate": 1, "Sand Stream":2, "Sand Veil":3, "Dry Skin":4, "Heat Proof":5} 
    yes_no_dict = {"Yes": 2, "No":1}
    team_examples = team_examples.drop(columns="Types")
    team_examples = team_examples.drop(columns="Name")
    team_examples["Type 2"] = team_examples["Type 2"].str.lower()
    team_examples["Type 1"] = team_examples["Type 2"].str.lower()
    team_examples["Type 1"] = team_examples["Type 1"].map(type_dict)
    team_examples["Type 2"] = team_examples["Type 2"].map(type_dict)
    team_examples["Ability 1"] = team_examples["Ability 1"].map(ability_dict)
    team_examples["Ability 2"] = team_examples["Ability 2"].map(ability_dict)
    team_examples["Complete Tank"] = team_examples["Complete Tank"].map(yes_no_dict)
    team_examples["All Rounder"] = team_examples["All Rounder"].map(yes_no_dict)
    team_examples["Support"] = team_examples["Support"].map(yes_no_dict)
    team_examples["Legendary"] = team_examples["Legendary"].map(yes_no_dict)
    team_examples["Complete Attacker"] = team_examples["Complete Attacker"].map(yes_no_dict)
    team_examples["Attacker"] = team_examples["Attacker"].map(yes_no_dict)
    team_examples["Special Attacker"] = team_examples["Special Attacker"].map(yes_no_dict)

    team_examples["Defense Tank"] = team_examples["Defense Tank"].map(yes_no_dict)
    team_examples["Special Defense Tank"] = team_examples["Special Defense Tank"].map(yes_no_dict)
    team_examples = team_examples.fillna(0).astype('int')

    features = list(team_examples.columns)
    features.remove("Chosen Team")
    X = team_examples[features]
    y = team_examples['Chosen Team']
    y = y.astype('int')
            
    ###################################################
            
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X,y)
            
    ###################################################
            
    def run_test(x):
        
        try: 
            del team_list[0:]
            weakness_list.clear()
            strength_list.clear()

            team_builder(x)
            team_list_grab_from_data1 = data[data["Name"].str.lower() == team_list[0]]
            team_list_grab_from_data1

            team_list_grab_from_data2 = data[data["Name"] == team_list[1]]
            team_list_grab_from_data2

            team_list_grab_from_data3 = data[data["Name"] == team_list[2]]
            team_list_grab_from_data3

            team_list_grab_from_data4 = data[data["Name"] == team_list[3]]
            team_list_grab_from_data4

            team_list_grab_from_data5 = data[data["Name"] == team_list[4]]
            team_list_grab_from_data5

            team_list_grab_from_data6 = data[data["Name"] == team_list[5]]

            concat_list = [team_list_grab_from_data1, team_list_grab_from_data2, team_list_grab_from_data3, team_list_grab_from_data4, 
                team_list_grab_from_data5, team_list_grab_from_data6]

            team_list_grab_from_data = pd.concat(concat_list)
            team_list_grab_from_data = team_list_grab_from_data.drop(columns="Name")
            team_list_grab_from_data["Type 1"] = team_list_grab_from_data["Type 1"].str.lower().map(type_dict)
            team_list_grab_from_data["Type 2"] = team_list_grab_from_data["Type 2"].str.lower().map(type_dict)
            team_list_grab_from_data["Complete Tank"] = team_list_grab_from_data["Complete Tank"].map(yes_no_dict)
            team_list_grab_from_data["All Rounder"] = team_list_grab_from_data["All Rounder"].map(yes_no_dict)
            team_list_grab_from_data["Support"] = team_list_grab_from_data["Support"].map(yes_no_dict)
            team_list_grab_from_data["Legendary"] = team_list_grab_from_data["Legendary"].map(yes_no_dict)
            team_list_grab_from_data["Complete Attacker"] = team_list_grab_from_data["Complete Attacker"].map(yes_no_dict)
            team_list_grab_from_data["Attacker"] = team_list_grab_from_data["Attacker"].map(yes_no_dict)
            team_list_grab_from_data["Special Attacker"] = team_list_grab_from_data["Special Attacker"].map(yes_no_dict)
            team_list_grab_from_data["Defense Tank"] = team_list_grab_from_data["Defense Tank"].map(yes_no_dict)
            team_list_grab_from_data["Special Defense Tank"] = team_list_grab_from_data["Special Defense Tank"].map(yes_no_dict)
            team_list_grab_from_data["Ability 1"] = team_list_grab_from_data["Ability 1"].map(ability_dict)
            team_list_grab_from_data["Ability 2"] = team_list_grab_from_data["Ability 2"].map(ability_dict)
            team_list_grab_from_data = team_list_grab_from_data.fillna(0)
            global result
            result = clf.predict(team_list_grab_from_data)
            print(result)
        except IndexError:
            pass
    while True:
        try:
            run_test(chosen_poke)
            if result == [2, 2, 2, 2, 2, 2]:
                print(result)
                break
        except ValueError:
            print(result)
            break
            

        