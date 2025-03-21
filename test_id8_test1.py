import pytest
from unittest.mock import patch
from computer import CPU, Memory

def test_cpu_loading_storing():
    memory = Memory()
    program = [1075, 1078, 1080, 2078, 2175, 2075, 1175, 1178, 1180, 4300]  
    for i, instruction in enumerate(program):
        memory.set(i, instruction)
    
    inputs = iter(['12','7','32'])
    def mock_input(prompt):
        return next(inputs)
    
    output = []
    def mock_output(message):
        output.append(message)

    cpu = CPU(memory, mock_output,mock_input)
    cpu.execute()
    
    assert memory.get(75) == 7
    assert memory.get(78) == 7
    assert memory.get(80) == 32
    assert cpu.accumulator == 7

    
