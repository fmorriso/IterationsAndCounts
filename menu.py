# Project 3.2.3 - Combo Menu Iteration with Loops
# Author: Fred Morrison
# Date written: 2023-03-10
# Description: A class that encapsulates all aspects of the menu of available food and beverages


# The menu of available items.
# structure:
#   first level is the item category.
#   second level is the type/size and corresponding price unless
#   there is only one type/size in which case the price is associate
#   with the category, such as ketchup.

Menu = {
    'sandwich': {
        'chicken': 5.25,
        'beef': 6.25,
        'tofu': 5.75
    },
    'beverage': {
        'small': 1.00,
        'medium': 1.75,
        'large': 2.25
    },
    'fries': {
        'small': 1.00,
        'medium': 1.50,
        'large': 2.00
    },
    'ketchup': 0.25
}
