# Зчитуємо матрицю з введення користувача
def read_matrix():
    rows, columns = map(int, input().split())
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix

# Додаємо дві матриці
def add_matrices():
    print("Enter size of first matrix:")
    matrix_a = read_matrix()

    print("Enter size of second matrix:")
    matrix_b = read_matrix()

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("The operation cannot be performed.")
        return

    result = []
    for i in range(len(matrix_a)):
        row = [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
        result.append(row)

    print("The result is:")
    for row in result:
        print(' '.join(map(str, row)))

# Множимо матрицю на константу
def multiply_by_constant():
    print("Enter size of matrix:")
    matrix = read_matrix()

    constant = float(input("Enter constant: "))

    result = [[element * constant for element in row] for row in matrix]

    print("The result is:")
    for row in result:
        print(' '.join(map(str, row)))

# Множимо дві матриці
def multiply_matrices():
    print("Enter size of first matrix:")
    matrix_a = read_matrix()

    print("Enter size of second matrix:")
    matrix_b = read_matrix()

    if len(matrix_a[0]) != len(matrix_b):
        print("The operation cannot be performed.")
        return

    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            cell_value = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
            row.append(cell_value)
        result.append(row)

    print("The result is:")
    for row in result:
        print(' '.join(map(str, row)))

# Транспонуємо матрицю
def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")

    choice = input("Your choice: ")

    print("Enter matrix size:")
    matrix = read_matrix()

    if choice == "1":
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif choice == "2":
        result = [row[::-1] for row in matrix[::-1]]
    elif choice == "3":
        result = [row[::-1] for row in matrix]
    elif choice == "4":
        result = matrix[::-1]
    else:
        print("Invalid choice.")
        return

    print("The result is:")
    for row in result:
        print(' '.join(map(str, row)))

# Обчислюємо визначник матриці
def calculate_determinant(matrix):
    size = len(matrix)

    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(size):
            submatrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
            determinant += (-1) ** j * matrix[0][j] * calculate_determinant(submatrix)
        return determinant

# Знаходимо зворотну матрицю
def inverse_matrix():
    print("Enter matrix size:")
    matrix = read_matrix()

    if len(matrix) != len(matrix[0]):
        print("The matrix must be square to find the inverse.")
        return

    determinant = calculate_determinant(matrix)
    if determinant == 0:
        print("This matrix doesn't have an inverse.")
        return

    size = len(matrix)
    adjoint_matrix = []

    for i in range(size):
        row = []
        for j in range(size):
            submatrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            cofactor = (-1) ** (i + j) * calculate_determinant(submatrix)
            row.append(cofactor)
        adjoint_matrix.append(row)

    inverse = [[adjoint_matrix[j][i] / determinant for j in range(size)] for i in range(size)]

    print("The result is:")
    for row in inverse:
        print(' '.join(map(str, row)))

# Основна функція
def main():
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            determinant()
        elif choice == "6":
            inverse_matrix()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter again.")

if __name__ == "__main__":
    main()
