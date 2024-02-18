import random

def generate_question(level):
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        answer = eval(question)
    elif level == 2:
        num = random.randint(11, 29)
        question = f"{num}^2"
        answer = num ** 2
    return question, answer

def main():
    correct_answers = 0
    total_questions = 5

    while True:
        level = input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> ")
        try:
            level = int(level)
            if level not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Incorrect format.")

    for _ in range(total_questions):
        question, answer = generate_question(level)
        while True:
            user_answer = input(f"{question}\n> ")
            try:
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Incorrect format.")

        if user_answer == answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/{total_questions}.")

    save_result = input("Would you like to save the result? Enter yes or no.\n> ").lower()
    if save_result in ['yes', 'y']:
        name = input("What is your name?\n> ")
        with open("results.txt", "a") as file:
            file.write(f"{name}: {correct_answers}/{total_questions} in level {level} ")
            if level == 1:
                file.write("(simple operations with numbers 2-9).\n")
            elif level == 2:
                file.write("(integral squares of 11-29).\n")
        print("The results are saved in \"results.txt\".")
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
