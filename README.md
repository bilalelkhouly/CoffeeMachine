# Coffee Machine Simulator

This Python project is a simple coffee machine simulator that allows users to order and dispense coffee drinks. It follows a set of requirements and features a text-based interface for interacting with the coffee machine. The program prompts the user to make a selection, checks resources, processes coins, and dispenses coffee while keeping track of resources and profits.

## Features

- Order a variety of coffee drinks, including espresso, latte, and cappuccino.
- Check and report the current state of resources (water, milk, coffee, and money).
- Automatically turn off the coffee machine with the "off" command.
- Check if there are sufficient resources to make the selected drink.
- Process coins (quarters, dimes, nickels, pennies) to pay for the drink.
- Check the success of the transaction and provide change if necessary.
- Make the selected coffee drink and deduct the required resources.
- Display a message to the user after the coffee is made.

## Usage

1. Run the `coffee_machine.py` script using Python:

   ```
   python coffee_machine.py
   ```

2. The program will prompt you with "What would you like? (espresso/latte/cappuccino):" to make a selection.

3. You can enter one of the following commands:
   - "espresso" to order an espresso.
   - "latte" to order a latte.
   - "cappuccino" to order a cappuccino.
   - "off" to turn off the coffee machine.
   - "report" to generate a report of current resources and profits.

4. When you choose a coffee drink, the program will prompt you to insert coins, and you can enter the number of quarters, dimes, nickels, and pennies.

5. The program will calculate the total amount of money inserted and check if it's sufficient to purchase the drink.

6. If the transaction is successful, the coffee will be made, resources will be deducted, and you will receive a message stating, "Here is your [drink]. Enjoy!"

## Requirements

- Python 3.12

## Credits

This project was created by Bilal Elkhouly

---

Feel free to customize and expand upon this project as needed. Enjoy your coffee and have fun!
