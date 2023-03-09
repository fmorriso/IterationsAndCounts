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
        return 'TODO: *** CODE NEEDED HERE ***'

    def ask_sandwich_choice(self):
        total: float = self.selections[Order.TOTAL_IDX]
        sandwich_cost: float = 0
        category = 'sandwich'
        sandwich = ''

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
            if sandwich.startswith('c'):
                sandwich = 'chicken'
                sandwich_cost = Order.menu[category][sandwich]
                waitingForChoice = False
            elif sandwich.startswith('b'):
                sandwich = 'beef'
                sandwich_cost = Order.menu[category][sandwich]
                waitingForChoice = False
            elif sandwich.startswith('t'):
                sandwich = 'tofu'
                sandwich_cost = Order.menu[category][sandwich]
                waitingForChoice = False
            else:
                print("You must choose a sandwich. Try again.")

        self.selections[Order.SANDWICH_IDX] = sandwich
        self.costs[Order.SANDWICH_IDX] = sandwich_cost
        self.selections[Order.TOTAL_IDX] += sandwich_cost
