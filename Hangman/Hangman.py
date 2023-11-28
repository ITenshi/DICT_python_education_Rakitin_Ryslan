import random

# hangman.py

def display_game_announcement():
    print("HANGMAN")
    print("The game will be available soon.")

def display_partial_word(secret_word, correct_guesses):
    # Виведення часткового слова з розкритими літерами та дефісами залишкових літер
    partial_word = ''.join(letter if letter in correct_guesses else '-' for letter in secret_word)
    print(f"{partial_word}\n")

def is_valid_input(letter):
    # Перевірка, чи введено правильну літеру
    return letter.isalpha() and letter.islower() and len(letter) == 1

def play_hangman():
    # Список слів для вибору
    word_list = ['python', 'java', 'javascript', 'php']

    # Випадково обираємо слово зі списку
    secret_word = random.choice(word_list)

    # Лічильник помилок
    mistakes_left = 8

    # Список вгаданих літер
    correct_guesses = set()

    while mistakes_left > 0:
        # Виведення часткового слова
        display_partial_word(secret_word, correct_guesses)

        # Введення гравцем літери
        letter = input("Input a letter: > ").lower()

        # Перевірка валідності введення
        if not is_valid_input(letter):
            print("Please enter a lowercase English letter")
            continue

        # Перевірка, чи буква вже вгадана
        if letter in correct_guesses:
            print("You've already guessed this letter")
        elif letter in secret_word:
            print("No improvements")
            correct_guesses.add(letter)
        else:
            print("That letter doesn't appear in the word")
            mistakes_left -= 1

        # Перевірка на виграш
        if set(secret_word) == correct_guesses:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            print("You survived!")
            break

    # Повідомлення про програш
    if mistakes_left == 0:
        print("\nThanks for playing! You ran out of attempts.")
        print(f"The correct word was: {secret_word}")

# Функція для взаємодії з менюм
def hangman_menu():
    while True:
        print("\nType \"play\" to play the game, \"exit\" to quit:")
        choice = input("> ").lower()

        if choice == "play":
            play_hangman()
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Please enter \"play\" or \"exit\".")

# Виклик функції для вигляду анонсу гри
display_game_announcement()

# Виклик функції для меню та гри
hangman_menu()
