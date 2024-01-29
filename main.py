from art import logo
from machine_data import MENU as menu
from machine_data import resources

print(logo)



# TODO 2. Print a report of all coffee machine resources and amount in till
def print_resources():
    print(f"Available Resources:\n"
          f"Water in ml: {resources.get('water')}\n"
          f"Milk in ml: {resources.get('milk')}\n"
          f"Coffee in ml: {resources.get('coffee')}\n"
          f"Matcha in ml: {resources.get('matcha')}\n"
          f"Amount in Register: ${bank}\n")

def avail_resources(drink):
    for item in drink:
        if drink[item] >= resources[item]:
            print(drink[item])
            print(f'Sorry there is not enough {item}.')
        else:
            print(f'Your {drink} is coming right up!')


# espresso = menu["espresso"]
# latte = menu["latte"]
# cappuccino = menu["cappuccino"]
# matcha = menu["matcha_latte"]

# keep track of amount in register
bank = 0

machine = True
while machine:
    choice = int(input("Welcome to the pantry! What drink would you like to choose? \n"
                      "Espresso = 1 / Latte = 2 / Cappuccino = 3 / Matcha = 4: "))
    if choice == 1:
        espresso = menu["espresso"]
        avail_resources(espresso['ingredients'])
        print(f"Espresso ingredients are: {espresso['ingredients']} and it cost ${espresso['cost']}")
        print(espresso['ingredients'])
    elif choice == 2:
        latte = menu["latte"]
        avail_resources(latte['ingredients'])
        print(f"Latte ingredients are: {latte['ingredients']} and it cost ${latte['cost']}")
        print_resources()
    elif choice == 3:
        cappuccino = menu["cappuccino"]
        avail_resources(cappuccino['ingredients'])
        print(f"Cappuccino ingredients are: {cappuccino['ingredients']} and it cost ${cappuccino['cost']}")
        print_resources()
    elif choice == 4:
        matcha = menu["matcha_latte"]
        avail_resources(matcha['ingredients'])
        print(f"Matcha Latte ingredients are: {matcha['ingredients']} and it cost ${matcha['cost']}")
        print_resources()
    # printing resources or shutting down machine
    elif choice == 5:
        print_resources()

    elif choice == 0:
        print("I'm shutting down now. See Ya!")
        machine = False



# TODO 3. Check for sufficient resources when a choice is ordered
# TODO 4. Prompt user to enter proper amount of $ when choice is selected and resources are confirmed
# TODO 6. Make choice for user
# TODO 7. Turn off machine with user input: "off"

