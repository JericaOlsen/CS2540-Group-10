import pytest
from unittest.mock import patch
from main import CPU, Memory

@pytest.fixture
def memory():
    return Memory()

@pytest.fixture
def cpu(memory):
    return CPU(memory)

def test_branching_with_negative_accumulator(cpu, memory):
    instructions = [1088, 1089, 1050, 3088, 3189, 4150, 4300]
    for i, instruction in enumerate(instructions):
        memory.set(i, instruction)
    inputs = iter([3, 9, 22])
    
    with patch('builtins.input', lambda _: next(inputs)):
        cpu.execute()
    assert cpu.accumulator == -6, "Accumulator should be -6 after operations"
    assert cpu.cr == 50, "CPU should have branched to location 50 due to negative accumulator"
