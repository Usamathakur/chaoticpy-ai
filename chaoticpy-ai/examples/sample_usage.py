# chaoticpy/examples/sample_usage.py

# Sample Usage of Chaoticpy-ai Library

# Import necessary modules/classes from the library
from chaoticpy.core.chaotic_numbers import ChaoticNumber
from chaoticpy.utils.helper_functions import calculate_mean

# Example usage of ChaoticNumber class
def demonstrate_chaotic_number_usage():
    # Creating chaotic numbers
    num1 = ChaoticNumber(2, 3)
    num2 = ChaoticNumber(4, 5)

    # Performing arithmetic operations
    result_addition = num1.add(num2)
    result_multiplication = num1.multiply(num2)

    # Displaying results
    print("Addition Result:", result_addition)
    print("Multiplication Result:", result_multiplication)

# Example usage of helper functions
def demonstrate_helper_function_usage():
    # A sample chaotic set
    chaotic_set = [3, 5, 8, 11, 15]

    # Calculating mean of the chaotic set using helper function
    mean = calculate_mean(chaotic_set)

    # Displaying mean
    print("Mean of Chaotic Set:", mean)

if __name__ == "__main__":
    # Demonstrate the usage of ChaoticNumber class
    demonstrate_chaotic_number_usage()

    # Demonstrate the usage of helper functions
    demonstrate_helper_function_usage()
