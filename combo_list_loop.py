# Project 3.2.3 - Combo Menu Iteration with Loops
# Author: Fred Morrison
# Date written: 2023-03-08
# Description: Modify the Combo Menu code using the loop of your choice to make it so that
#              the user has the option to keep entering more orders.
import sys

from order import Order

orders: list[Order] = []


# generate a single order
def getOrder() -> Order:
    order: Order = Order()
    order.ask_sandwich_choice()
    order.ask_beverage_choice()
    order.ask_fries_choice()
    order.ask_ketchup_choice()
    order.check_for_discount()
    return order


# main program starts here
def getOrders():
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


# give user the option to review every order
def ask_to_review_orders():
    reviewOrders: bool = False
    needYesNoDecision: bool = True
    while needYesNoDecision:
        yn: str = input('Do you want to see all of the orders?>').lower()
        match yn[0:1]:
            case 'y':
                needYesNoDecision = False
                reviewOrders = True
            case 'n':
                needYesNoDecision = False
            case _:
                print('Invalid response. Valid responses are yes or no. Try again.')

    if reviewOrders:
        print('Here are all of the orders:')
        print('-' * 20)
        order: Order = []
        for order in orders:
            print(order)
            print('-' * 20)


if __name__ == '__main__':
    print(
        f'Using Python version {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} release level {sys.version_info.releaselevel}')

    getOrders()
    ask_to_review_orders()
