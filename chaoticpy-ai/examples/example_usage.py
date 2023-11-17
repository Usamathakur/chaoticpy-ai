# examples/example_usage.py

from chaoticpy_ai.core import ChaoticNumber

# Example usage of the ChaoticPy AI Library
chaotic_num1 = ChaoticNumber(2)
chaotic_num2 = ChaoticNumber(3)

# Perform operations
result_add = chaotic_num1.add(chaotic_num2)
result_multiply = chaotic_num1.multiply(chaotic_num2)

print("Result of addition:", result_add.value)
print("Result of multiplication:", result_multiply.value)
