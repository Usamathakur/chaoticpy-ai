import random

class ChaoticNumber:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return ChaoticNumber(self.value + other.value)

    def multiply(self, other):
        # Multiply chaotic numbers by generating a random factor
        random_factor = random.uniform(0.5, 2.0)
        return ChaoticNumber(self.value * other.value * random_factor)
