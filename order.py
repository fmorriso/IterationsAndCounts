class Order:
    order_id: int = 0

    # positional indexes within the order and costs lists
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

    # constructor
    def __init__(self):
        Order.order_id += 1
        self.selections = ["", "", "", 0, 0.0]
        self.costs: list[float] = [0.0, 0.0, 0.0, 0.0]

    # toString()
    def __str__(self) -> str:
        tostring: str = 'Your order:\n'

        # include sandwich selection and cost
        if self.selections[Order.SANDWICH_IDX] != '':
            tostring += f'A {self.selections[Order.SANDWICH_IDX]} sandwich for ${self.costs[Order.SANDWICH_IDX]:.2f}\n'

        # include beverage size and cost
        if self.selections[Order.BEVERAGE_IDX] != '':
            tostring += f'A {self.selections[Order.BEVERAGE_IDX]} beverage for ${self.costs[Order.BEVERAGE_IDX]:.2f}\n'

        # include french fries size and cost
        if self.selections[Order.FRIES_IDX] != '':
            tostring += f'A {self.selections[Order.FRIES_IDX]} order of french fries for ${self.costs[Order.FRIES_IDX]:.2f}\n'

        # include total cost of the order
        tostring += f'Total: ${self.selections[Order.TOTAL_IDX]:.2f}'
        return tostring

    def ask_sandwich_choice(self):
        category = 'sandwich'
        price: float = 0
        sandwich: str = ''

        # build the choices prompt
        choices = 'Which type of sandwich:  '
        for choice in Order.menu[category]:
            price = Order.menu[category][choice]
            choices += f'{choice}: ${price:.2f}, '
        # remove trailing comma and replace with question mark
        choices = f"{choices.removesuffix(', ')}?>"

        waitingForChoice: bool = True
        while waitingForChoice:
            sandwich = input(choices).lower()           
            match sandwich[0:1]:
                case 'c':
                    sandwich = 'chicken'
                    price = Order.menu[category][sandwich]
                    waitingForChoice = False
                case 'b':
                    sandwich = 'beef'
                    price = Order.menu[category][sandwich]
                    waitingForChoice = False
                case 't':
                    sandwich = 'tofu'
                    price = Order.menu[category][sandwich]
                    waitingForChoice = False
                case _:
                    print("You must choose a sandwich. Try again.")

        self.selections[Order.SANDWICH_IDX] = sandwich
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
            for choice in Order.menu[category]:
                price = Order.menu[category][choice]
                choices += f'{choice}: ${price:.2f}, '
            # remove trailing comma and replace with question mark
            choices = f"{choices.removesuffix(', ')}?>"

            waitingForSize: bool = True
            while waitingForSize:
                response = input(choices).lower()
                match response[0:1]:
                    case 's':
                        size = "small"
                        price = Order.menu[category][size]
                        waitingForSize = False
                    case 'm':
                        size = "medium"
                        price = Order.menu[category][size]
                        waitingForSize = False
                    case 'l':
                        size = "large"
                        price = Order.menu[category][size]
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
        madeSelection: bool = False

        needYesNoChoice: bool = True
        while needYesNoChoice:
            response = input("Would you like fries? (yes or no):>").lower()
            match response[0:1]:
                case 'y':            
                    needYesNoChoice = False
                    madeSelection = True
                case 'n':
                    needYesNoChoice = False
                case _:
                    print('Invalid response. Valid responses are yes or no.  Try again.')

            if madeSelection:
                # build choices prompt
                choices = 'What size french-fries would you like? '
                for choice in Order.menu[category]:
                    size = choice
                    price = Order.menu[category][choice]
                    choices += f'{size}: ${price:.2f}, '
                # remove trailing comma and replace with question mark
                choices = f"{choices.removesuffix(', ')}?>"

                needChoice = True
                while needChoice:
                    response = input(choices).lower()
                    match response[0:1]:
                        case 's':
                            size = 'small'
                            needChoice = False
                            price = Order.menu[category][size]
                            mega_size = input("Would you like to MEGA-Size your fries? (yes or no): ").lower()
                            if mega_size.startswith('y'):
                                size = "large"
                                price += 1                        
                        case 'm':
                            size = "medium"
                            price = Order.menu[category][size]                        
                            needChoice = False
                        case 'l':
                            size = "large"
                            price = Order.menu[category][size]                       
                            needChoice = False
                        case _:
                            print('invalid choice. try again')

                      
                self.selections[Order.FRIES_IDX] = size
                self.costs[Order.FRIES_IDX] = price
                self.selections[Order.TOTAL_IDX] += price  
