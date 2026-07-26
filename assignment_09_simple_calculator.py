def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """
    Returns the division result rounded to 2 decimal places.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return round(a / b, 2)


def modulus(a, b):
    """
    Returns the remainder of division.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulus with zero.")
    return a % b


def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b


def display_menu():
    """Displays the main menu options."""
    print("\n============================")
    print("     SIMPLE CALCULATOR      ")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_numbers():
    """
    Helper function to safely prompt and retrieve two numeric inputs from the user.
    """
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number: "))
    # Format to int if the number is whole, otherwise leave as float
    num1 = int(num1) if num1.is_integer() else num1
    num2 = int(num2) if num2.is_integer() else num2
    return num1, num2


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Error: Invalid option. Please enter a number between 1 and 7.")
            continue

        try:
            num1, num2 = get_numbers()

            if choice == "1":
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")

            elif choice == "2":
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")

            elif choice == "3":
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")

            elif choice == "4":
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")

            elif choice == "5":
                result = modulus(num1, num2)
                print(f"Result: {num1} % {num2} = {result}")

            elif choice == "6":
                result = power(num1, num2)
                print(f"Result: {num1} ** {num2} = {result}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Invalid numeric input. Please enter valid numbers.")


if __name__ == "__main__":
    main()