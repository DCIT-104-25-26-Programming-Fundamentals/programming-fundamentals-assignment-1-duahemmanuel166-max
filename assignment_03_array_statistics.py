# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================


def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def find_minimum(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def main():
    # Read total count from user
    n = int(input("How many numbers? "))

    # Validate that N is a positive integer
    if n <= 0:
        print("Error: The number of items must be a positive integer.")
        return

    numbers = []

    # Read user input into list
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        # Convert to integer if it's a whole number for clean output matching the example
        if num.is_integer():
            num = int(num)
        numbers.append(num)

    # Calculate statistics using separate functions
    total = calculate_sum(numbers)
    avg = calculate_average(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)

    # Display results
    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {avg}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


if __name__ == "__main__":
    main()