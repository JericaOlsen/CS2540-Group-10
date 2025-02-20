import pytest
from unittest.mock import patch
from main import CPU, Memory

def test_cpu_loading_storing():
    memory = Memory()
    cpu = CPU(memory)
    program = [1075, 1078, 1080, 2078, 2175, 2075, 1175, 1178, 1180, 4300]  
    for i, instruction in enumerate(program):
        memory.set(i, instruction)
    
    user_inputs = ["12", "7", "32"]  

    with patch("builtins.input", side_effect=user_inputs), patch("builtins.print") as mock_print:
        cpu.execute()
    
    assert memory.get(75) == 7
    assert memory.get(78) == 7
    assert memory.get(80) == 32
    assert cpu.accumulator == 7

    mock_print.assert_any_call("Value at memory[75]: 7")
    mock_print.assert_any_call("Value at memory[78]: 7")
    mock_print.assert_any_call("Value at memory[80]: 32")
    mock_print.assert_any_call("Program halted.")
