import numpy as np

# Safe integer input
def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print(" Please enter a valid integer.")

# Matrix input function
def input_matrix(name):
    rows = get_int(f"Enter number of rows for {name}: ")
    cols = get_int(f"Enter number of columns for {name}: ")

    print(f"Enter elements of {name} row by row (space separated):")
    matrix = []

    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) != cols:
                    print(f" Please enter exactly {cols} values.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print(" Please enter numeric values only.")

    return np.array(matrix)

# Menu
def show_menu():
    print("\n------ MATRIX OPERATIONS TOOL ------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

# Input matrices
A = input_matrix("Matrix A")
B = input_matrix("Matrix B")

# Operations loop
while True:
    show_menu()
    choice = get_int("Enter your choice: ")

    if choice == 1:
        print("\nResult of A + B:")
        print(A + B)

    elif choice == 2:
        print("\nResult of A - B:")
        print(A - B)

    elif choice == 3:
        print("\nResult of A × B:")
        print(np.dot(A, B))

    elif choice == 4:
        print("\nTranspose of Matrix A:")
        print(A.T)

    elif choice == 5:
        print("\nDeterminant of Matrix A:")
        print(np.linalg.det(A))

    elif choice == 6:
        print("\nExiting Matrix Operations Tool...")
        break

    else:
        print(" Invalid choice. Try again.")
