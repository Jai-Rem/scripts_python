import json
import random

def read_values_from_json(key):
    values = []
    with open("characters.json") as f:
    	data = json.load(f)
        # load all the data contained in this file. data = entries
        for entry in data:
            values.append(entry[key])
    return values

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb] # get a quote from a list
    return item # return the item


def random_character():
	all_values = read_values_from_json("character")
	return get_random_item_in(all_values)

#print(read_values_from_json("character"))
print(random_character())