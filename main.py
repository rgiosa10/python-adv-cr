from faker import Faker
import json

fake = Faker()

value_or_more = 4

# Use Python's Faker library to generate a list of twenty colors. Call it color_list.
color_list = [fake.color_name() for item in range(20)]

# Function to remove any duplicates from color_list.
def remove_dups(list_input:list):
    """ Validates that argument is list, and if so removes duplicate items, and returns list without duplicates

    Args:
        list_input (list): list with strings as items

    Returns:
        list: Returns list that is absent any duplicates, or if argument was incorrect returns False
    """
    if not list_input:
        return False
    if isinstance(list_input, list):
        color_dict_no_duplicates = {color: None for color in list_input}
        color_list_no_duplicates = list(color_dict_no_duplicates.keys())
        return color_list_no_duplicates
    else:
        return False

color_list = remove_dups(color_list)

if color_list == False:
    print("Please input a list with strings inside")
else:
    # Dictionary comprehension to create a dict from color_list (no duplicates) 
    color_dict = {color: len(color) for color in color_list}

    # Write color_dict to JSON file
    with open("./data/color_data.json", "w") as json_file:
        json.dump(color_dict, json_file)

    # Read color_dict back out of the JSON file
    with open("./data/color_data.json", "r") as json_file:
        color_dict = json.load(json_file)

        # Print string saying the color name and length of name, if value is value_or_more or greater
        greater_four_values = [print(f"{key}: length of color name is {value}") for key, value in color_dict.items() if value >= value_or_more]