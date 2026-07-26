def generate_fibonacci(n):
    """
    Generates and returns a list containing the first n terms 
    of the Fibonacci sequence using an iterative loop.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]
    for _ in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence


def is_fibonacci(num):
    """
    Checks if a non-negative integer belongs to the Fibonacci sequence 
    using an iterative loop.
    """
    if num < 0:
        return False

    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    return a == num


def part_a():
    """
    Handles PART A: Asking user for N and printing the first N terms.
    """
    try:
        n = int(input("How many terms? "))
        if n <= 0:
            print("Error: Please enter a positive integer greater than 0.")
            return

        terms = generate_fibonacci(n)
        # Convert list of numbers to space-separated string
        print("Fibonacci sequence:", " ".join(map(str, terms)))

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


def part_b():
    """
    Handles PART B: Checking if a user-entered number belongs to the sequence.
    """
    try:
        num = int(input("Enter a number to check: "))
        if num < 0:
            print(f"{num} is NOT a Fibonacci number.")
            return

        if is_fibonacci(num):
            print(f"{num} is a Fibonacci number.")
        else:
            print(f"{num} is NOT a Fibonacci number.")

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


def main():
    print("--- PART A ---")
    part_a()

    print("\n--- PART B ---")
    part_b()


if __name__ == "__main__":
    main()