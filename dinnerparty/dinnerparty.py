# dinnerparty.py

import random


def get_friends():
    try:
        # Зчитати кількість друзів
        num_friends = int(input("Enter the number of friends joining (including you):\n"))

        if num_friends <= 0:
            print("No one is joining for the party")
            return {}

        # Зчитати імена друзів
        friends = {}
        print("Enter the name of every friend (including you), each on a new line:")
        for _ in range(num_friends):
            name = input("> ")
            friends[name] = 0  # Ініціалізувати борг кожного друга нулем

        return friends

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return {}


def split_bill(friends, total_amount):
    if not friends:
        print("No one is joining for the party")
        return

    try:
        # Зчитати загальний рахунок
        total_amount = float(input("Enter the total amount:\n"))

        # Перевірити, чи введений рахунок дорівнює 0 або менше
        if total_amount <= 0:
            print("Invalid total amount. Please enter a positive value.")
            return

        # Розділити рахунок порівну між усіма друзями
        share_per_person = round(total_amount / len(friends), 2)

        # Оновити значення у словнику
        for friend in friends:
            friends[friend] = share_per_person

        # Вивести оновлений словник
        print(friends)

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def choose_lucky_one(friends):
    if not friends:
        print("No one is joining for the party")
        return

    try:
        # Запитайте користувача, чи хоче він вибрати "щасливчика"
        choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower()

        if choice == 'yes':
            # Вибрати випадковим чином ім'я зі словника
            lucky_one = random.choice(list(friends.keys()))
            print(f"{lucky_one} is the lucky one!")

            # Перерахувати суму для кожного, крім "щасливчика"
            for friend in friends:
                if friend != lucky_one:
                    friends[friend] = round(friends[friend] + friends[lucky_one], 2)

            # Обнулити "щасливчика"
            friends[lucky_one] = 0

            # Вивести оновлений словник
            print(friends)
        else:
            print("No one is going to be lucky")

    except ValueError:
        print("Invalid input. Please enter a valid choice.")


if __name__ == "__main__":
    # Викликати функції
    friends_dict = get_friends()
    split_bill(friends_dict, 0)  # Початковий рахунок може бути будь-яким числом
    choose_lucky_one(friends_dict)
