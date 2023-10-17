from inventory import MENU, resources

profit = 0


# Coffee Machine Program


def print_report(machine_resources):
    """Prints a report of all coffee machine resources"""
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def check_transaction_success(money_received, drink_cost):
    """Returns True when payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def process_coins():
    """Returns the total calculated from coins inserted"""
    total = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total += (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    return total


is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print_report(resources)
    else:
        drink = MENU[user_choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction_success(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
