from faker import Faker
import json

fake = Faker()

value_or_more = 4
color_list = [fake.color_name() for item in range(20)]

print(f"{len(color_list)}: {color_list}")

def remove_dups(list_input:list) -> list:
    """ Validates that argument is list, and if so removes duplicate items, and returns list without duplicates

    Args:
        list_input (list): list of strings

    Returns:
        list: Returns list that is absent any duplicates, or if argument was incorrect returns False
    """
    if not list_input:
        return False
    elif isinstance(list_input, list):
        color_dict_no_duplicates = {color: None for color in list_input}
        color_list_no_duplicates = list(color_dict_no_duplicates.keys())
        return color_list_no_duplicates
    else:
        return False

color_list = remove_dups(color_list)
print(f"{len(color_list)}: {color_list}")

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

        greater_four_values = [print(f"{key}: length of color name is {value}") for key, value in color_dict.items() if value >= value_or_more]