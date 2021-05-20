import csv
import json
import pandas as pd

# Initialize empty lists
global team_list
team_list = []

pokemon_type = []
# with is a keyword used when working with unmanaged resources
# clean up the resource 
# open the file and read it, define it as csvfile
with open('../src/csvs/turtwig_training.csv', 'r') as csvfile:
    with open('./water.json', 'w') as jsonfile:
        # create a list data structure which is mutable
        pokemon = list(csv.reader(csvfile))
        # remove the header
        pokemon = pokemon[1:]
        # We use the csv library to create a 'reader' of the file
        # This reader patse through the csvfile and the headers 
        # and allow us to interact with it as a Python object
        # reader = csv.DictReader(csvfile, fieldnames)
        # This creates an empty dictionary to hold the final set of 
        # data that we'll eventually dump into the JSON file
        final_data = {}
        # use for loop to iterate over every row of our data
        # our print will print strings rather than numbers
        # need to convert the "number" values to actual numbers
        for poke in pokemon:
            poke[1] = int(poke[1])
        
        # want to print out all the water type pokemon
        for poke_type in pokemon:
            po = poke_type[3]
            
            if po == 'Water':
                pokemon_type.append(poke_type)
                continue
            for row in pokemon_type:

                final_data[ len(pokemon_type)] ={ 
                    "pokemon_data": {
                        "Types" : row[0],
                        "Sdex" : row[1],   
                        "Name" : row[2],                 
                        "Type 1" : row[3],
                        "Type 2" : row[4],
                        "HP": row[5]
                    }
                   
                }
            
        json.dump(final_data, jsonfile)
        # And then we write a final newline to the end of the file 
        # (this is just a best practice)
        jsonfile.write('\n')
    
        # show pokemon results
        #print(pokemon[:5])
            
        # print fire_team
        print(pokemon_type)
        print(final_data)