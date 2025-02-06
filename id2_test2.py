import pytest
from id2_test1 import load_instructions_and_data
from main import CPU, Memory  

@pytest.fixture
def setup_cpu():
    """Fixture to initialize CPU and Memory for testing."""
    memory = Memory()
    cpu = CPU(memory)
    return cpu, memory

def test_store_and_write_new_binary_message(setup_cpu, capsys):
    """Test that a different binary message is stored and printed correctly."""
    cpu, memory = setup_cpu

    # Instructions as given in the use case
    instructions = [1020,1021,1022,1023,1024,1025,1026,1027, 
                    1120,1121,1122,1123,1124,1125,1126,1127, 4300]

    # New binary message (converted to decimal representation)
    new_binary_message = [0, 1, 3, 2, 5, 7, 4, 2]  # '00 01 11 10 101 111 100 010'

    # Load instructions and new binary message into memory
    load_instructions_and_data(memory, instructions, 30, new_binary_message)

    # Verify stored values in memory
    for i, value in enumerate(new_binary_message):
        assert memory.get(30 + i) == value, f"Memory at {30 + i} should be {value}"

    for i in range(30, 38):
        cpu.write(i)

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")

    expected_output = [f"Value at memory[{30 + i}]: {new_binary_message[i]}" for i in range(len(new_binary_message))]

    assert output_lines == expected_output, f"\nExpected:\n{expected_output}\nGot:\n{output_lines}"

