import pytest
from io import StringIO
from unittest.mock import patch
from main import CPU, Memory

def test_loading_and_storing():
    memory = Memory()
    cpu = CPU(memory)
    
    # Load initial instructions into memory
    program = [1075, 1078, 1080, 2078, 2175, 2075, 1175, 1178, 1180, 4300]
    for i, instr in enumerate(program):
        memory.set(i, instr)
    
    # Mock user input (Teacher enters 12, 7, 32)
    inputs = iter(["12", "7", "32"])
    
    with patch('builtins.input', lambda _: next(inputs)):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            cpu.execute()
            output = mock_output.getvalue()
    
    # Check expected memory values
    assert memory.get(75) == 7
    assert memory.get(78) == 7
    assert memory.get(80) == 32
    
    # Verify printed output
    expected_output = """Value at memory[75]: 7\nValue at memory[78]: 7\nValue at memory[80]: 32\nProgram halted.\n"""
    assert expected_output in output
