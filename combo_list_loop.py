# Project 3.2.3 - Combo Menu Iteration with Loops
# Author: Fred Morrison
# Date written: 2023-03-08
# Description: Modify the Combo Menu code using the loop of your choice to make it so that
#              the user has the option to keep entering more orders.
import sys

from order import Order

orders: list[Order] = []


# generate a single order
def get_order() -> Order:
    order: Order = Order()
    order.ask_sandwich_choice()
    order.ask_beverage_choice()
    order.ask_fries_choice()
    order.ask_ketchup_choice()
    order.check_for_discount()
    return order


# main program starts here
def get_orders():
    keepOrdering: bool = True
    while keepOrdering:

        order = get_order()
        orders.append(order)
        print(order)

        need_yes_no_choice: bool = True
        while need_yes_no_choice:
            yn: str = input('Do you want to make another order?>').lower()
            """
            match yn[0:1]:
                case 'y':
                    needYesNoChoice = False
                case 'n':
                    needYesNoChoice = False
                    keepOrdering = False
                case _:
                    print('Invalid response.  Valid responses are yes or no')
            """
            yn = yn[0:1]
            if yn == 'y':
                need_yes_no_choice = False
            elif yn == 'n':
                need_yes_no_choice = False
                keepOrdering = False
            else:
                print('Invalid response.  Valid responses are yes or no')



# give user the option to review every order
def ask_to_review_orders():
    review_orders: bool = False
    need_yes_no_decision: bool = True
    while need_yes_no_decision:
        yn: str = input('Do you want to see all of the orders?>').lower()
        match yn[0:1]:
            case 'y':
                need_yes_no_decision = False
                review_orders = True
            case 'n':
                need_yes_no_decision = False
            case _:
                print('Invalid response. Valid responses are yes or no. Try again.')

    if review_orders:
        print('Here are all of the orders:')
        print('-' * 20)
        order: Order = []
        for order in orders:
            print(order)
            print('-' * 20)


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

if __name__ == '__main__':
    print(f'Using Python version {get_python_version()}')


    get_orders()
    ask_to_review_orders()
