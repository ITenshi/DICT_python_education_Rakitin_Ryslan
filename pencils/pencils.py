# pencils_game.py
import random

def get_num_pencils():
    while True:
        try:
            num_pencils = int(input("How many pencils would you like to use:\n> "))
            if num_pencils <= 0:
                print("The number of pencils should be positive")
                continue
            return num_pencils
        except ValueError:
            print("The number of pencils should be numeric")

def get_first_player():
    while True:
        player1 = input("Who will be the first (John, Jack):\n> ").capitalize()
        if player1 not in ['John', 'Jack']:
            print("Choose between 'John' and 'Jack'")
            continue
        return player1

def print_pencils(num_pencils):
    print("|" * num_pencils)

def bot_move(num_pencils):
    if num_pencils % 4 == 0:
        return random.randint(1, 3)
    else:
        return num_pencils % 4

def main():
    num_pencils = get_num_pencils()
    first_player = get_first_player()

    while num_pencils > 0:
        print_pencils(num_pencils)
        print(f"{first_player}'s turn:")

        if first_player == 'Jack':
            move = bot_move(num_pencils)
            print(move)
        else:
            while True:
                try:
                    move = int(input("> "))
                    if move not in [1, 2, 3]:
                        print("Possible values: '1', '2' or '3'")
                        continue
                    if move > num_pencils:
                        print("Too many pencils were taken")
                        continue
                    break
                except ValueError:
                    print("Possible values: '1', '2' or '3'")

        num_pencils -= move
        first_player = "John" if first_player == "Jack" else "Jack"

    print(f"{first_player} won!")

if __name__ == "__main__":
    main()
