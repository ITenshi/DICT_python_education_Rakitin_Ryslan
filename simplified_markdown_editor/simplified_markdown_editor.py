# Функція для виведення довідкового повідомлення
def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list line-break")
    print("Special commands: !help !done")

# Функція для обробки введення заголовка
def process_header():
    while True:
        level = int(input("Level: > "))
        if 1 <= level <= 6:
            return '#' * level
        else:
            print("The level should be within the range of 1 to 6.")

# Функція для обробки введення посилання
def process_link():
    label = input("Label: > ")
    url = input("URL: > ")
    return f"[{label}]({url})"

# Функція для обробки введення списку
def process_list():
    while True:
        num_rows = int(input("Number of rows: > "))
        if num_rows > 0:
            break
        else:
            print("The number of rows should be greater than zero.")

    items = []
    for i in range(num_rows):
        item = input(f"Row #{i + 1}: > ")
        items.append(item)

    return items

# Основна функція програми
def markdown_editor():
    formatted_text = ""
    while True:
        user_input = input("Choose a formatter: > ")

        # Перевірка на спеціальні команди
        if user_input == "!help":
            print_help()
        elif user_input == "!done":
            print("Final Markdown Text:")
            print(formatted_text)
            # Збереження результатів у файл output.md
            with open("output.md", "w") as file:
                file.write(formatted_text)
            print("Output saved to output.md")
            print("Program terminated.")
            break
        # Перевірка на форматування
        elif user_input in ["plain", "bold", "italic", "inline-code", "line-break"]:
            text = input("Text: > ")
            if user_input == "plain":
                formatted_text += text
            elif user_input == "bold":
                formatted_text += f"**{text}**"
            elif user_input == "italic":
                formatted_text += f"*{text}*"
            elif user_input == "inline-code":
                formatted_text += f"`{text}`"
            elif user_input == "line-break":
                formatted_text += '\n'
            print(formatted_text)
        elif user_input == "header":
            text = input("Text: > ")
            formatted_text += f"{process_header()} {text}\n"
            print(formatted_text)
        elif user_input == "link":
            formatted_text += process_link() + '\n'
            print(formatted_text)
        elif user_input == "ordered-list":
            items = process_list()
            formatted_text += '\n'.join([f"{i + 1}. {item}" for i, item in enumerate(items)]) + '\n'
            print(formatted_text)
        elif user_input == "unordered-list":
            items = process_list()
            formatted_text += '\n'.join([f"* {item}" for item in items]) + '\n'
            print(formatted_text)
        else:
            print("Unknown formatting type or command")

# Виклик функції програми
markdown_editor()
