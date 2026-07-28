# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, cols):
    """Read a matrix of size rows x cols from the user, one row per line."""
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) != cols:
                print(f"Error: Row must contain exactly {cols} value(s). Try again.")
                continue
            try:
                row = [float(value) for value in row_input]
            except ValueError:
                print("Error: Please enter numbers only. Try again.")
                continue
            matrix.append(row)
            break
    return matrix


def print_matrix(matrix, title="Matrix"):
    """Display a matrix in a neat, aligned grid format."""
    print(f"\n{title}:")
    for row in matrix:
        formatted_row = []
        for value in row:
            # Show whole numbers without a decimal point
            if value == int(value):
                formatted_row.append(f"{int(value):>5}")
            else:
                formatted_row.append(f"{value:>5}")
        print(" ".join(formatted_row))


def transpose_matrix(matrix):
    """Return the transpose of the given matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product A x B using nested loops."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


def get_dimensions(prompt_rows="Enter number of rows: ", prompt_cols="Enter number of columns: "):
    """Read and validate positive integer dimensions from the user."""
    while True:
        try:
            rows = int(input(prompt_rows))
            cols = int(input(prompt_cols))
            if rows <= 0 or cols <= 0:
                print("Error: Dimensions must be positive integers.")
                continue
            return rows, cols
        except ValueError:
            print("Error: Please enter valid whole numbers.")


def part_a_transpose():
    print("\n--- Part A: Transpose a Matrix ---")
    rows, cols = get_dimensions()
    matrix = read_matrix(rows, cols)

    print_matrix(matrix, "Original Matrix")
    transposed = transpose_matrix(matrix)
    print_matrix(transposed, "Transposed Matrix")


def part_b_add():
    print("\n--- Part B: Add Two Matrices ---")
    rows, cols = get_dimensions()

    print("\nMatrix A:")
    matrix_a = read_matrix(rows, cols)

    print("\nMatrix B (must be the same size):")
    matrix_b = read_matrix(rows, cols)

    result = add_matrices(matrix_a, matrix_b)

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
    print_matrix(result, "Sum (A + B)")


def part_c_multiply():
    print("\n--- Part C: Multiply Two Matrices ---")
    print("Matrix A (size M x N):")
    rows_a, cols_a = get_dimensions()
    matrix_a = read_matrix(rows_a, cols_a)

    print("\nMatrix B (size N x P — rows must equal columns of A):")
    rows_b, cols_b = get_dimensions()

    if rows_b != cols_a:
        print(f"Error: Number of rows in B ({rows_b}) must equal number of columns in A ({cols_a}).")
        return

    matrix_b = read_matrix(rows_b, cols_b)

    result = multiply_matrices(matrix_a, matrix_b)

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
    print_matrix(result, "Product (A x B)")


def main():
    print("Matrix Operations Menu")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")

    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_add()
    elif choice == "3":
        part_c_multiply()
    else:
        print("Error: Please choose a valid option (1, 2, or 3).")


if __name__ == "__main__":
    main()