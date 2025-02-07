import pytest
from unittest.mock import patch
from main import CPU, Memory

# Test class for CPU branching behavior
def test_cpu_branching():
    memory = Memory()
    cpu = CPU(memory)

    # Load the program into memory
    program = [1088, 1089, 1050, 3088, 3189, 4150, 4300]  # Program instructions
    for i, instruction in enumerate(program):
        memory.set(i, instruction)
    
    # Simulate input values for memory[88] = 3 and memory[89] = 9
    user_inputs = ["3", "9", "22"]
    
    with patch("builtins.input", side_effect=user_inputs), patch("builtins.print") as mock_print:
        cpu.execute()
    
    # Verify memory is set correctly
    assert memory.get(88) == 3 
    assert memory.get(89) == 9
    
    # Verify accumulator operations
    assert cpu.accumulator == -6
    
    # Verify control register jumps to location 50 after branch
    print(f'Control Register after branching: {cpu.cr}')
    assert cpu.cr == 50

    mock_print.assert_any_call("You have branched to location50")
