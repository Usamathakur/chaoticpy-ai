# tests/test_core.py

from chaoticpy_ai.core import ChaoticNumber

def test_add():
    chaotic_num1 = ChaoticNumber(2)
    chaotic_num2 = ChaoticNumber(3)
    result = chaotic_num1.add(chaotic_num2)
    assert result.value == 5

def test_multiply():
    chaotic_num1 = ChaoticNumber(2)
    chaotic_num2 = ChaoticNumber(3)
    result = chaotic_num1.multiply(chaotic_num2)
    assert result.value == 6
