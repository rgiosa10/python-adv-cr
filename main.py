from faker import Faker
import json

fake = Faker()

color_list = []

for item in range(20): 
    color = fake.color_name()
    color_list.append(color)

#print(f"{len(color_list)}: {color_list}")

def remove_dups(list_input:list) -> list:
    """ Takes in a list, removes duplicate items, and returns list without duplicates

    Args:
        list_input (list): list of strings

    Returns:
        list: Returns list that is absent any duplicates
    """
    if not list_input:
        return False
    elif isinstance(list_input, list):
        color_list_no_duplicates = list(set(list_input)) # Remove duplicates by converting to set then back to list
        return color_list_no_duplicates
    else:
        return False

color_list = remove_dups(color_list)
#print(f"{len(color_list)}: {color_list}")

if color_list == False:
    print("Please input a list with strings inside")
else:
    color_dict = {color: len(color) for color in color_list}
    print(color_dict)

    with open("./data/color_data.json", "w") as json_file:
        json.dump(color_dict, json_file)

    with open("./data/color_data.json", "r") as json_file:
        color_dict = json.load(json_file)
        print(color_dict)

        greater_four_values = [print(f"{key}: length of color name is {value}") for key, value in color_dict.items() if value >= 4]