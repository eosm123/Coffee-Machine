MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_rss(flavour, water, milk, coffee):
    if water < MENU[flavour]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif flavour != "espresso" and milk < MENU[flavour]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif coffee < MENU[flavour]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


flavour = input("What would you like? (espresso/latte/cappuccino): ")
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
profit = 0

while flavour != "off":
    # TODO: 1. Print report. (how much water/milk left etc.)
    if flavour == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${profit}")
    # TODO: 2. Check if resources are sufficient.
    elif flavour == "espresso" or flavour == "latte" or flavour == "cappuccino":
        if check_rss(flavour, water, milk, coffee) == True:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
    # TODO: 3. Process coins
            value = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    # TODO: 4. Check if transaction is successful
            change = 0
            if value > MENU[flavour]["cost"]:
                change = value - MENU[flavour]["cost"]
                print(f"Here is ${round(change, 2)} in change.")
    # TODO: 5. Make coffee and deduct resources
                water -= MENU[flavour]["ingredients"]["water"]
                coffee -= MENU[flavour]["ingredients"]["coffee"]
                profit += MENU[flavour]["cost"]
                if flavour != "espresso":
                    milk -= MENU[flavour]["ingredients"]["milk"]
                print(f"Here is your {flavour}. Enjoy!")
            else:
                print("Sorry that is not enough money. Money has been refunded.")
    flavour = input("What would you like? (espresso/latte/cappuccino): ")

#notes: option + shift to multiline edit
# control + r to run