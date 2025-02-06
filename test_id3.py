from io import StringIO
from main import Memory, CPU

def test_id3_1(monkeypatch):
    """
        Test input
    """
    memory = Memory()
    cpu = CPU(memory)

    for i, instruction in enumerate([1007, 1008, 1009, 3007, 3108, 3009, 4300]):
         memory.set(i, instruction)

    monkeypatch.setattr('sys.stdin', StringIO("28\n5\n4\n"))
    cpu.execute()
    
    assert memory.get(7) == 28
    assert memory.get(8) == 5
    assert memory.get(9) == 4


def test_id3_2(monkeypatch):
    """
        Test result
    """
    memory = Memory()
    cpu = CPU(memory)

    for i, instruction in enumerate([1007, 1008, 1009, 3007, 3108, 3009, 4300]):
         memory.set(i, instruction)

    monkeypatch.setattr('sys.stdin', StringIO("28\n5\n4\n"))
    cpu.execute()
    assert cpu.accumulator == 27

