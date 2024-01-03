from art import logo
from machine_data import MENU as menu
from machine_data import resources

print(logo)

# TODO 1. Prompt user by asking "What type of would you like?"


# TODO 2. Print a report of all coffee machine resources
def print_resources():
    print(f"Available Resources:\n"
          f"Water in ml: {resources.get('water')}\n"
          f"Milk in ml: {resources.get('milk')}\n"
          f"Coffee in ml: {resources.get('coffee')}\n"
          f"Matcha in ml: {resources.get('matcha')}\n")


espresso = menu.get("espresso")
latte = menu.get("latte")
cappuccino = menu.get("cappuccino")
matcha = menu.get("matcha_latte")

machine = True
while machine:
    choice = int(input("Welcome to the pantry! What would you like to choice? \n"
                      "Espresso = 1 / Latte = 2 / Cappuccino = 3 / Matcha = 4: "))
    if choice == 1:
        print(f"Espresso ingredients are: {espresso['ingredients']} and it cost ${espresso['cost']}")
        print_resources()
    elif choice == 2:
        print(f"Latte ingredients are: {latte.get('ingredients')} and it cost ${latte.get('cost')}")
        print_resources()
    elif choice == 3:
        print(f"Cappuccino ingredients are: {cappuccino.get('ingredients')} and it cost ${cappuccino.get('cost')}")
        print_resources()
    elif choice == 4:
        print(f"Matcha Latte ingredients are: {matcha.get('ingredients')} and it cost ${matcha.get('cost')}")
        print_resources()
    elif choice == 0:
        print("I'm shutting down now. See Ya!")
        machine = False



# TODO 3. Check for sufficient resources when a choice is ordered
# TODO 4. Prompt user to enter proper amount of $ when choice is selected and resources are confirmed
# TODO 6. Make choice for user
# TODO 7. Turn off machine with user input: "off"

