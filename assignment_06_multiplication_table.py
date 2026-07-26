def print_single_table(num):
    """
    Prints the multiplication table for a given number from 1 to 12.
    """
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num:2d}  x  {i:2d}  =  {num * i:3d}")


def part_a():
    """
    Handles PART A: Single Table generation.
    """
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Error: Please enter a positive integer.")
            return

        print_single_table(num)

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


def part_b():
    """
    Handles PART B: Generating tables from 1 to N.
    """
    try:
        n = int(input("Enter N (to display tables from 1 to N): "))
        if n <= 0:
            print("Error: Please enter a positive integer.")
            return

        for i in range(1, n + 1):
            print_single_table(i)
            if i < n:
                print("-" * 30)

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


def main():
    print("--- PART A ---")
    part_a()

    print("\n--- PART B ---")
    part_b()


if __name__ == "__main__":
    main()