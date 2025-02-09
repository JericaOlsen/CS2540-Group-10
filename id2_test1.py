import pytest
from main import CPU, Memory  

@pytest.fixture
def setup_cpu():
    memory = Memory()
    cpu = CPU(memory)
    return cpu, memory

def load_instructions_and_data(memory, instructions, data_start, data_values):
    for i, instr in enumerate(instructions):
        memory.set(i, instr)

    for i, value in enumerate(data_values):
        memory.set(data_start + i, value)

def test_store_binary_message(setup_cpu):
    cpu, memory = setup_cpu
    instructions = [1020,1021,1022,1023,1024,1025,1026,1027, 
                    1120,1121,1122,1123,1124,1125,1126,1127, 4300]

    binary_message = [1, 0, 2, 0, 1, 6, 10, 1]

    load_instructions_and_data(memory, instructions, 20, binary_message)

    for i, value in enumerate(binary_message):
        assert memory.get(20 + i) == value, f"Memory at {20 + i} should be {value}"

def test_write_binary_message(setup_cpu, capsys):
    cpu, memory = setup_cpu

    instructions = [1020,1021,1022,1023,1024,1025,1026,1027, 
                    1120,1121,1122,1123,1124,1125,1126,1127, 4300]

    binary_message = [1, 0, 2, 0, 1, 6, 10, 1]

    load_instructions_and_data(memory, instructions, 20, binary_message)

    for i in range(20, 28):
        cpu.write(i)

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")

    expected_output = [f"Value at memory[{20 + i}]: {binary_message[i]}" for i in range(len(binary_message))]

    assert output_lines == expected_output, f"\nExpected:\n{expected_output}\nGot:\n{output_lines}"
