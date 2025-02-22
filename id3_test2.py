from io import StringIO
from computer import Memory, CPU

def test_id3_2(monkeypatch):
    """
        Test result
    """
    memory = Memory()
    cpu = CPU(memory, print, input)

    for i, instruction in enumerate([1007, 1008, 1009, 3007, 3108, 3009, 4300]):
         memory.set(i, instruction)

    monkeypatch.setattr('sys.stdin', StringIO("28\n5\n4\n"))
    cpu.execute()
    assert cpu.accumulator == 27
