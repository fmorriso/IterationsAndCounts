# Project 3.2.3 - Combo Menu Iteration with Loops
# Author: Fred Morrison
# Date written: 2023-03-08
# Description: Modify the Combo Menu code using the loop of your choice to make it so that
#              the user has the option to keep entering more orders.

import sys

from order import Order


def getOrder():
    order: Order = Order()
    order.ask_sandwich_choice()
    order.ask_beverage_choice()
    order.ask_fries_choice()
    order.ask_ketchup_choice()
    order.check_for_discount()
    return order


# main program starts here
def getOrders():
    orders: list[Order] = []
    keepOrdering: bool = True
    while keepOrdering:
        order = getOrder()
        orders.append(order)
        print(order)
        needYesNoChoice: bool = True
        while needYesNoChoice:
            yn: str = input('Do you want to make another order?>').lower()
            match yn[0:1]:
                case 'y':
                    needYesNoChoice = False
                case 'n':
                    needYesNoChoice = False
                    keepOrdering = False
                case _:
                    print('Invalid response.  Valid responses are yes or no')


def getOrdersNew():
    #  sandwich = 0, beverage = 1, fries = 2, ketchup =3, total = 4
    order = ["", "", "", 0, 0.0]
    costs: list[float] = [0.0, 0.0, 0.0, 0.0]
    SANDWICH_IDX = 0
    BEVERAGE_IDX = 1
    FRIES_IDX = 2
    KETCHUP_IDX = 3
    TOTAL_IDX = 4

    menu = {
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


if __name__ == '__main__':
    print(
        f'Using Python version {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} release level {sys.version_info.releaselevel}')

    getOrders()
