def is_prime(number):
    """
    Checks if a number is prime.
    Returns True if prime, False otherwise.
    """
    # Numbers less than 2 are not prime
    if number < 2:
        return False
        
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Found a divisor, so it is not prime
            
    return True  # No divisors found, so it is prime

# Main block to handle user input and display output
if __name__ == "__main__":
    # Get input from the user and convert it to an integer
    user_input = int(input("Enter a number: "))
    
    # Call the function and print the exact expected output format
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is NOT a prime number.")