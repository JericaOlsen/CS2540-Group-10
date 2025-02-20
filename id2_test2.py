import pytest
from id2_test1 import load_instructions_and_data
from main import CPU, Memory  

@pytest.fixture
def setup_cpu():
    memory = Memory()
    cpu = CPU(memory)
    return cpu, memory

def test_store_and_write_new_binary_message(setup_cpu, capsys):
    cpu, memory = setup_cpu

    instructions = [1020,1021,1022,1023,1024,1025,1026,1027, 
                    1120,1121,1122,1123,1124,1125,1126,1127, 4300]

    new_binary_message = [0, 1, 3, 2, 5, 7, 4, 2]

    load_instructions_and_data(memory, instructions, 30, new_binary_message)

    for i, value in enumerate(new_binary_message):
        assert memory.get(30 + i) == value, f"Memory at {30 + i} should be {value}"

    for i in range(30, 38):
        cpu.write(i)

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")

    expected_output = [f"Value at memory[{30 + i}]: {new_binary_message[i]}" for i in range(len(new_binary_message))]

    assert output_lines == expected_output, f"\nExpected:\n{expected_output}\nGot:\n{output_lines}"

