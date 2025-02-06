#!/usr/bin/env python3
# Author: Edison Leung
# Author ID: 147724231
# Date Created: 2025/02/06

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # accepts two lists as arguments keys and values, combines these lists together to create a dictionary
    # returns a dictionary that has the keys and associated values from the lists
    new_dict = {}  # Initialize an empty dictionary
    i = 0
    while i < len(keys):  # Use a while loop to iterate through the lists
        new_dict[keys[i]] = values[i]  # Assign the value to the key
        i += 1
    return new_dict

def shared_values(dict1, dict2):
    # accepts two dictionaries as arguments and finds all values that are shared between the two dictionaries
    # returns a set containing ONLY values found in BOTH dictionaries
    values1 = set(dict1.values())  # Create a set of values from dict1
    values2 = set(dict2.values())  # Create a set of values from dict2
    return values1 & values2  # Return the intersection (common values) as a set


if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)
