# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def calculate_sum(numbers):
    """Return the sum of all numbers in the list, without using sum()."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Return the average of the numbers in the list."""
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_max(numbers):
    """Return the largest number in the list, without using max()."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def calculate_min(numbers):
    """Return the smallest number in the list, without using min()."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def get_numbers(n):
    """Prompt the user to enter n numbers and return them as a list."""
    numbers = []
    for i in range(1, n + 1):
        value = float(input(f"Enter number {i}: "))
        numbers.append(value)
    return numbers


def main():
    n_input = input("How many numbers? ")

    try:
        n = int(n_input)
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = get_numbers(n)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_max(numbers)
    minimum = calculate_min(numbers)

    # Print numbers as ints when they are whole, to match example formatting
    def fmt(x):
        return int(x) if x == int(x) else x

    print("\nResults:")
    print(f"Sum:     {fmt(total)}")
    print(f"Average: {average}")
    print(f"Maximum: {fmt(maximum)}")
    print(f"Minimum: {fmt(minimum)}")


if __name__ == "__main__":
    main()