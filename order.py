# Project 3.2.3 - Combo Menu Iteration with Loops
# Author: Fred Morrison
# Date written: 2023-03-08
# Description: A class that encapsulates all aspects of a single order
# Modifications:
#   2023-03-15 - made loading of menu selections from external file private.


import json

from size import Size


class Order:
    Menu = {}
    order_id: int = 0

    # positional indexes within the order and costs lists
    SANDWICH_IDX = 0
    BEVERAGE_IDX = 1
    FRIES_IDX = 2
    KETCHUP_IDX = 3
    TOTAL_IDX = 4

    # constructor
    def __init__(self):
        Order.order_id += 1
        self.orderId = Order.order_id
        self.selections = ["", "", "", 0, 0.0]
        self.costs: list[float] = [0.0, 0.0, 0.0, 0.0]
        self.gets_discount: bool = False
        # pull in menu when first order is created
        if len(Order.Menu) == 0:
            Order.__loadMenu()

    # private static method to load the menu selections from an external flat file.
    # Called only once when the very first order is created since the menu is a
    # shared resource available to any/all orders.
    @staticmethod
    def __loadMenu():
        # pull in the menu from a JSON file
        with open("menu.json", "r") as read_file:
            Order.Menu = json.load(read_file)

    # toString()
    def __str__(self) -> str:
        tostring: str = f'Order #{self.orderId}:\n'

        # include sandwich selection and cost
        if self.selections[Order.SANDWICH_IDX] != '':
            tostring += f'A {self.selections[Order.SANDWICH_IDX]} sandwich for ${self.costs[Order.SANDWICH_IDX]:.2f}\n'

        # include beverage size and cost
        if self.selections[Order.BEVERAGE_IDX] != '':
            tostring += f'A {self.selections[Order.BEVERAGE_IDX]} beverage for ${self.costs[Order.BEVERAGE_IDX]:.2f}\n'

        # include french fries size and cost
        if self.selections[Order.FRIES_IDX] != '':
            tostring += f'A {self.selections[Order.FRIES_IDX]} order of french fries for ${self.costs[Order.FRIES_IDX]:.2f}\n'

        # include ketchup packets count and cost
        if self.selections[Order.KETCHUP_IDX] > 0:
            tostring += f'{self.selections[Order.KETCHUP_IDX]} ketchup packets for ${self.costs[Order.KETCHUP_IDX]:.2f}\n'

        # show discount message when applicable
        if self.gets_discount:
            subtotal: float = self.selections[Order.TOTAL_IDX] + 1
            tostring += f'Subtotal before discount: ${subtotal:.2f}\n'
            tostring += 'You received a discount of $1 because you ordered a combo.\n'

        # include total cost of the order
        tostring += f'Total: ${self.selections[Order.TOTAL_IDX]:.2f}'
        return tostring

    def ask_sandwich_choice(self):
        category: str = 'sandwich'
        price: float = 0
        sandwichChoice: str = ''

        # build the choices prompt
        choices = 'Which type of sandwich:  '
        for choice in Order.Menu[category]:
            price = Order.Menu[category][choice]
            choices += f'{choice}: ${price:.2f}, '
        # remove trailing comma and replace with question mark
        choices = f"{choices.removesuffix(', ')}?>"

        waitingForChoice: bool = True
        while waitingForChoice:
            sandwichChoice = input(choices).lower()
            match sandwichChoice[0:1]:
                case 'c':
                    sandwichChoice = 'chicken'
                    price = Order.Menu[category][sandwichChoice]
                    waitingForChoice = False
                case 'b':
                    sandwichChoice = 'beef'
                    price = Order.Menu[category][sandwichChoice]
                    waitingForChoice = False
                case 't':
                    sandwichChoice = 'tofu'
                    price = Order.Menu[category][sandwichChoice]
                    waitingForChoice = False
                case _:
                    print("You must choose a sandwich. Try again.")

        self.selections[Order.SANDWICH_IDX] = sandwichChoice
        self.costs[Order.SANDWICH_IDX] = price
        self.selections[Order.TOTAL_IDX] += price

    def ask_beverage_choice(self):
        category: str = 'beverage'
        price: float = 0
        selected_a_beverage: bool = False
        size: str = ''

        needYesNoChoice: bool = True
        while needYesNoChoice:
            response: str = input("Would you like a beverage? (yes or no): >").lower()
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
            for choice in Order.Menu[category]:
                price = Order.Menu[category][choice]
                choices += f'{choice}: ${price:.2f}, '
            # remove trailing comma and replace with question mark
            choices = f"{choices.removesuffix(', ')}?>"

            waitingForSize: bool = True
            while waitingForSize:
                response = input(choices).lower()
                match response[0:1]:
                    case 's':
                        size = Size.SMALL.value
                        price = Order.Menu[category][size]
                        waitingForSize = False
                    case 'm':
                        size = Size.MEDIUM.value
                        price = Order.Menu[category][size]
                        waitingForSize = False
                    case 'l':
                        size = Size.LARGE.value
                        price = Order.Menu[category][size]
                        waitingForSize = False
                    case _:
                        print("Invalid beverage size, try again.")

            self.selections[Order.BEVERAGE_IDX] = size
            self.costs[Order.BEVERAGE_IDX] = price
            self.selections[Order.TOTAL_IDX] += price

    def ask_fries_choice(self):
        category: str = 'fries'
        size: str = ''
        price: float = 0.0
        wantsFries: bool = False

        needYesNoChoice: bool = True
        while needYesNoChoice:
            response = input("Would you like fries? (yes or no):>").lower()
            match response[0:1]:
                case 'y':
                    needYesNoChoice = False
                    wantsFries = True
                case 'n':
                    needYesNoChoice = False
                case _:
                    print('Invalid response. Valid responses are yes or no.  Try again.')

            if wantsFries:
                # build choices prompt
                choices = 'What size french-fries would you like? '
                for choice in Order.Menu[category]:
                    size = choice
                    price = Order.Menu[category][choice]
                    choices += f'{size}: ${price:.2f}, '
                # remove trailing comma and replace with question mark
                choices = f"{choices.removesuffix(', ')}?>"

                needChoice = True
                while needChoice:
                    response = input(choices).lower()
                    match response[0:1]:
                        case 's':
                            size = Size.SMALL.value
                            needChoice = False
                            price = Order.Menu[category][size]
                            mega_size = input("Would you like to MEGA-Size your fries? (yes or no): ").lower()
                            if mega_size.startswith('y'):
                                size = Size.LARGE.value
                                price += 1
                        case 'm':
                            size = Size.MEDIUM.value
                            price = Order.Menu[category][size]
                            needChoice = False
                        case 'l':
                            size = Size.LARGE.value
                            price = Order.Menu[category][size]
                            needChoice = False
                        case _:
                            print('invalid choice. try again')

                self.selections[Order.FRIES_IDX] = size
                self.costs[Order.FRIES_IDX] = price
                self.selections[Order.TOTAL_IDX] += price

    def ask_ketchup_choice(self):
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

        self.selections[Order.KETCHUP_IDX] = ketchupPackets
        if ketchupPackets > 0:
            price: float = ketchupPackets * Order.Menu[category]
            self.costs[Order.KETCHUP_IDX] = price
            self.selections[Order.TOTAL_IDX] += price

    def check_for_discount(self):
        if self.selections[Order.SANDWICH_IDX] == '' \
            or self.selections[Order.BEVERAGE_IDX] == '' \
            or    self.selections[Order.FRIES_IDX] == '':
            return
        self.gets_discount = True
        self.selections[Order.TOTAL_IDX] -= 1

    def add(self, a: int, b: int) -> int:
        return a + b