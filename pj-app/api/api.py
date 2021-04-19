# from flask import Flask

from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('../public/index.html', embed=example_embed)

app.run(debug=True)

# from flask import Flask, render_template, request
# import pandas as pd

# app = flask(_name_)

# @app.route('/'. methods=['GET', 'POST'])
# def index():
#     return render_template('index.html')

# @app.route('/data', methods=['GET', 'POST'])
#     def data():
#         if request.method == 'POST':
#             file = request.form['upload-file']
#             data = pd.read_excel(file)
#             return render_template('data.html', data=data)


# if _name_ == '_main_':
#     app.run(debug=true)

# # import the data and fill the NAN with zero
# data = pd.read_excel("pokemon dp list 1.xlsx")
# type_chart = pd.read_excel("pokemon type chart.xlsx")
# data = data.fillna(0)

# global team_list
# team_list = []

# global weakness_list
# weakness_list =[]

# global strength_list
# strength_list = []

# pokemon_chooser()

# if chosen_poke == ["turtwig"]:
    
#     team_examples = pd.read_excel("pokemon turtwig training data draft.xlsx")
    

#     def team_builder(x):
        
#         x = x[0]
#         team_list.append(x)
#         grab_chosen_poke_name = data[data["Name"].str.lower() == team_list[0]]
#         grab_chosen_poke_type = grab_chosen_poke_name["Type 1"][0].lower()
#         type_chart_grab_1 = type_chart[type_chart["Attacking Type"] == grab_chosen_poke_type].drop(columns="Attacking Type")
#         type_column_names = type_chart_grab_1.columns.to_list()

#         for i in type_column_names:
#             if type_chart_grab_1[i].values == 0.5:
#                 weakness_list.append(i)

#         if len(weakness_list) > 5:
#             diff = len(weakness_list) - 5
#             for i in range(diff):
#                 weakness_list.pop(random.randrange(len(weakness_list)))
#         else: pass

#         print(weakness_list)

#         type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[0]]
#         for i in type_column_names:
#             if type_grab_2[i].values == 0.5:
#                 strength_list.append(i)

#         random_type = random.choice(strength_list)
#         poke_from_strength = data[data["Type 1"].str.lower() == random_type]
#         chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
#         team_list.append(chosen_type_poke)


#         type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[1]]
#         for i in type_column_names:
#             if type_grab_2[i].values == 0.5:
#                 strength_list.append(i)

#         random_type = random.choice(strength_list)
#         poke_from_strength = data[data["Type 1"].str.lower() == random_type]
#         chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
#         team_list.append(chosen_type_poke)

#         type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[2]]
#         for i in type_column_names:
#             if type_grab_2[i].values == 0.5:
#                 strength_list.append(i)

#         random_type = random.choice(strength_list)
#         poke_from_strength = data[data["Type 1"].str.lower() == random_type]
#         chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
#         team_list.append(chosen_type_poke)

#         type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[3]]
#         for i in type_column_names:
#             if type_grab_2[i].values == 0.5:
#                 strength_list.append(i)

#         random_type = random.choice(strength_list)
#         poke_from_strength = data[data["Type 1"].str.lower() == random_type]
#         chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
#         team_list.append(chosen_type_poke)

#         type_grab_2 = type_chart[type_chart["Attacking Type"] == weakness_list[4]]
#         for i in type_column_names:
#             if type_grab_2[i].values == 0.5:
#                 strength_list.append(i)

#         random_type = random.choice(strength_list)
#         poke_from_strength = data[data["Type 1"].str.lower() == random_type]
#         chosen_type_poke = random.choice(poke_from_strength["Name"].to_list())
#         team_list.append(chosen_type_poke)

#         print(team_list)

# elif chosen_poke == ["chimchar"]:
#    team_examples = pd.read_excel("chimchar training data draft.xlsx")
