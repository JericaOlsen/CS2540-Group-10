from unittest.mock import patch
from main import CPU, Memory

def test_cpu_branching():
    memory = Memory()
    cpu = CPU(memory)

    program = [1088, 1089, 1050, 3088, 3189, 4150, 4300]
    for i, instruction in enumerate(program):
        memory.set(i, instruction)
    
    user_inputs = ["3", "9", "22"]
    
    with patch("builtins.input", side_effect=user_inputs), patch("builtins.print") as mock_print:
        cpu.execute()
    
    assert memory.get(88) == 3 
    assert memory.get(89) == 9
    
    assert cpu.accumulator == -6
    
    print(f'Control Register after branching: {cpu.cr}')
    assert cpu.cr == 50

    mock_print.assert_any_call("You have branched to location50")
