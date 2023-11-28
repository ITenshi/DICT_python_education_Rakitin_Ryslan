class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def process_input(self, user_input):
        if user_input == "remaining":
            return self.get_status()
        elif user_input == "exit":
            return "Exiting the coffee machine"
        elif user_input == "buy":
            return self.buy_coffee()
        elif user_input == "fill":
            return self.fill_resources()
        elif user_input == "take":
            return self.take_money()
        else:
            return "Invalid input. Please enter a valid action."

    def get_status(self):
        return f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee_beans} of coffee beans\n{self.disposable_cups} of disposable cups\n{self.money} of money"

    def buy_coffee(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee_type == "back":
            return "Returning to main menu"

        coffee_type = int(coffee_type)
        if coffee_type not in [1, 2, 3]:
            return "Invalid coffee type. Please enter a valid option."

        if coffee_type == 1:  # espresso
            return self.make_coffee(250, 0, 16, 4)
        elif coffee_type == 2:  # latte
            return self.make_coffee(350, 75, 20, 7)
        elif coffee_type == 3:  # cappuccino
            return self.make_coffee(200, 100, 12, 6)

    def make_coffee(self, water_needed, milk_needed, beans_needed, cost):
        if self.water < water_needed:
            return "Sorry, not enough water!"
        elif self.milk < milk_needed:
            return "Sorry, not enough milk!"
        elif self.coffee_beans < beans_needed:
            return "Sorry, not enough coffee beans!"
        elif self.disposable_cups == 0:
            return "Sorry, not enough disposable cups!"

        self.water -= water_needed
        self.milk -= milk_needed
        self.coffee_beans -= beans_needed
        self.disposable_cups -= 1
        self.money += cost

        return "I have enough resources, making you a coffee!"

    def fill_resources(self):
        self.water += int(input("Write how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable cups of coffee you want to add:\n"))

        return "Refilling resources"

    def take_money(self):
        money_taken = self.money
        self.money = 0
        return f"I gave you {money_taken}"


# Використання класу CoffeeMachine
coffee_machine = CoffeeMachine()

while True:
    user_input = input("Write action (buy, fill, take, remaining, exit):\n")

    if user_input == "exit":
        break

    print(coffee_machine.process_input(user_input) + "\n")
