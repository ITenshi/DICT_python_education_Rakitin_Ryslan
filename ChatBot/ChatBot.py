# Отримання поточного року
import time
current_year = time.localtime().tm_year

# Обране ім'я для бота
bot_name = "DICT_Bot"

# Виведення привітання
print(f"Hello! My name is {bot_name}.")
print(f"I was created in {current_year}.")

# Запит користувача про його ім'я
print("Please, remind me your name.")
user_name = input("> ")

# Привітання користувача
print(f"What a great name you have, {user_name}!")

# Загадка віку
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")

# Підрахунок від 0 до введеного числа
print("Now I will prove to you that I can count to any number you want.")
user_number = int(input("Enter a positive number: "))

# Виведення підрахунку
for i in range(user_number + 1):
    print(i, end=' ')

# Завершення діалогу
print("\nWell, wasn't that impressive?")

# Питання для тестування
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

# Правильна відповідь
correct_answer = "2"

# Перевірка відповіді користувача
while True:
    user_answer = input("> ")
    if user_answer == correct_answer:
        break
    else:
        print("Please, try again.")

# Завершення програми
print("Congratulations, have a nice day!")
