from io import StringIO
from computer import Memory, CPU

def test_id6_2(monkeypatch):
    """
        Test result
    """
    memory = Memory()
    cpu = CPU(memory, print, input)

    for i, instruction in enumerate([1050, 1051, 2050, 3151, 4206, 1152, 4300]):
        memory.set(i, instruction)

    monkeypatch.setattr('sys.stdin', StringIO("5\n5\n"))
    cpu.execute()

    assert cpu.accumulator == 0
    assert cpu.cr == 6
