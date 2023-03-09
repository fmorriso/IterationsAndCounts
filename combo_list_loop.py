# Project 3.2.3 - Combo Menu Iteration with Loops
# Author: Fred Morrison
# Date written: 2023-03-08
# Description: Modify the Combo Menu code using the loop of your choice to make it so that
#              the user has the option to keep entering more orders.

import sys

from order import Order


def getSandwich(menu, costs, order, idx, total_idx):
    total = order[total_idx]
    sandwich_cost = 0
    category = 'sandwich'
    sandwich = ''

    # build the choices prompt
    choices = 'Which type of sandwich:  '
    for choice in menu[category]:
        price = menu[category][choice]
        choices += f'{choice}: ${price:.2f}, '
    # remove trailing comma and replace with question mark
    choices = f"{choices.removesuffix(', ')}?>"

    waitingForChoice = True
    while waitingForChoice:
        sandwich = input(choices).lower()
        if sandwich.startswith('c'):
            sandwich = 'chicken'
            sandwich_cost = menu[category][sandwich]
            waitingForChoice = False
        elif sandwich.startswith('b'):
            sandwich = 'beef'
            sandwich_cost = menu[category][sandwich]
            waitingForChoice = False
        elif sandwich.startswith('t'):
            sandwich = 'tofu'
            sandwich_cost = menu['sandwich'][sandwich]
            waitingForChoice = False
        else:
            print("You must choose a sandwich. Try again.")

    total += sandwich_cost
    order[idx] = sandwich
    costs[idx] = sandwich_cost
    order[total_idx] += total


def getFrenchFries(menu, costs, order, idx, total_idx):
    total: float = order[total_idx]
    selected_french_fries: bool = False
    size: str = ""
    category: str = 'fries'
    cost: float = 0.0

    needYesNoChoice = True
    while needYesNoChoice:
        french_fries = input("Would you like fries? (yes or no): ").lower()
        if french_fries.startswith('y'):
            needYesNoChoice = False
            selected_french_fries = True
        elif french_fries.startswith('n'):
            needYesNoChoice = False
        else:
            print('Invalid response. Valid responses are yes or no.  Try again.')

        if selected_french_fries:

            # build choices prompt
            choices = 'What size french-fries would you like? '
            for choice in menu[category]:
                size = choice
                price = menu[category][choice]
                choices += f'{size}: ${price:.2f}, '
            # remove trailing comma and replace with question mark
            choices = f"{choices.removesuffix(', ')}?>"

            needChoice = True
            while needChoice:
                response = input(choices).lower()
                if response.startswith('s'):
                    size = 'small'
                    needChoice = False
                    cost = menu[category][size]
                    mega_size = input("Would you like to MEGA-Size your fries? (yes or no): ").lower()
                    if mega_size.startswith('y'):
                        size = "large"
                        cost += 1
                    total += cost
                elif response.startswith('m'):
                    size = "medium"
                    cost = menu[category][size]
                    total += cost
                    needChoice = False
                elif response.startswith('l'):
                    size = "large"
                    cost = menu[category][size]
                    total += cost
                    needChoice = False
                else:
                    print('invalid choice. try again')

    order[total_idx] = total

    if selected_french_fries:
        order[idx] = size
        costs[idx] = cost


def getBeverage(menu, costs, order, idx, total_idx):
    total: float = order[total_idx]
    price: float = 0
    category: str = 'beverage'
    selected_a_beverage: bool = False
    size: str = ''

    needYesNoChoice: bool = True
    while needYesNoChoice:
        response: str = input("Would you like a beverage? (yes or no): ").lower()
        match response[0:1]:
            case 'y':
                needYesNoChoice = False
                selected_a_beverage = True
            case 'n':
                needYesNoChoice = False
            case _:
                print('Invalid response. Valid responses are yes or no.  Try again.')

    if selected_a_beverage:
        # build the choices prompt
        choices = 'What size beverage would you like? '
        for choice in menu[category]:
            price = menu[category][choice]
            choices += f'{choice}: ${price:.2f}, '
        # remove trailing comma and replace with question mark
        choices = f"{choices.removesuffix(', ')}?>"

        waitingForSize = True
        while waitingForSize:
            response = input(choices).lower()
            match response[0:1]:
                case 's':
                    size = "small"
                    price = menu[category][size]
                    waitingForSize = False
                case 'm':
                    size = "medium"
                    price = menu[category][size]
                    waitingForSize = False
                case 'l':
                    size = "large"
                    price = menu[category][size]
                    waitingForSize = False
                case _:
                    print("Invalid beverage size, try again.")

    if selected_a_beverage:
        order[idx] = size
        costs[idx] = price
        total += price

    order[total_idx] = total


def getKetchupPackets(menu, costs, order, idx, total_idx):
    total: float = order[total_idx]
    category: str = 'ketchup'
    ketchupPackets: int = 0

    needChoice: bool = True
    while needChoice:
        response = input("How many ketchup packets would you like (up to 10)? Enter 0 if you don't want any.>")
        if response.isnumeric() and 10 >= int(response) >= 0:
            needChoice = False
            ketchupPackets = int(response)
        else:
            print('Invalid response. Try again.')

    order[idx] = ketchupPackets
    if ketchupPackets > 0:
        costs[idx] = ketchupPackets * menu[category]
        total += costs[idx]

    order[total_idx] = total


def getOrder():
    order: Order = Order()
    order.ask_sandwich_choice()
    return order


# main program starts here
def getOrders():
    orders: list[Order] = []
    keepOrdering: bool = True
    while keepOrdering:
        order = getOrder()
        orders.append(order)
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
                    print('Invalid respsonse.  Valid responses are yes or no')

    for order in orders:
        print(order)

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

    getSandwich(menu, costs, order, SANDWICH_IDX, TOTAL_IDX)
    getBeverage(menu, costs, order, BEVERAGE_IDX, TOTAL_IDX)
    getFrenchFries(menu, costs, order, FRIES_IDX, TOTAL_IDX)
    getKetchupPackets(menu, costs, order, KETCHUP_IDX, TOTAL_IDX)

    printFinalOrder(BEVERAGE_IDX, FRIES_IDX, KETCHUP_IDX, SANDWICH_IDX, TOTAL_IDX, costs, order)


def printFinalOrder(BEVERAGE_IDX, FRIES_IDX, KETCHUP_IDX, SANDWICH_IDX, TOTAL_IDX, costs, order):
    print('Your order:')

    if order[SANDWICH_IDX] != "":
        print(f'A {order[SANDWICH_IDX]} sandwich for ${costs[SANDWICH_IDX]:.2f}')

    if order[BEVERAGE_IDX] != "":
        print(f'A {order[BEVERAGE_IDX]} beverage for ${costs[BEVERAGE_IDX]:.2f}')

    if order[FRIES_IDX] != "":
        print(f'A {order[FRIES_IDX]} order of french fries for ${costs[FRIES_IDX]:.2f}')

    if order[KETCHUP_IDX] > 0:
        print(f'{order[KETCHUP_IDX]} ketchup packets for ${costs[KETCHUP_IDX]:.2f}')

    # give a $1 discount if customer orders all three types of items
    if order[SANDWICH_IDX] != '' and order[BEVERAGE_IDX] != '' and order[FRIES_IDX] != '':
        print(f'order subtotal before discount: ${order[TOTAL_IDX]:.2f}')
        print(f'You received a $1.00 discount because you ordered all three types of menu items')
        order[TOTAL_IDX] -= 1.00

    print(f'Your final total order cost is ${order[TOTAL_IDX]:.2f}')


if __name__ == '__main__':
    print(
        f'Using Python version {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} release level {sys.version_info.releaselevel}')

    getOrders()
