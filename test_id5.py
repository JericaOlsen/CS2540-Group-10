from io import StringIO
from main import Memory, CPU


def test_id5_1(monkeypatch):
    """
        Test input
    """
    memory = Memory()
    cpu = CPU(memory)

    for i, instruction in enumerate([1088, 1089, 1050, 3088, 3189, 4150, 4300]):
        memory.set(i, instruction)

    monkeypatch.setattr('sys.stdin', StringIO("3\n9\n22\n"))
    cpu.execute()

    assert memory.get(88) == 3
    assert memory.get(89) == 9
    assert memory.get(50) == 22


def test_id5_2(monkeypatch):
    """
        Test result
    """
    memory = Memory()
    cpu = CPU(memory)

    for i, instruction in enumerate([1088, 1089, 1050, 3088, 3189, 4150, 4300]):
        memory.set(i, instruction)

    monkeypatch.setattr('sys.stdin', StringIO("3\n9\n22\n"))
    cpu.execute()
    assert cpu.accumulator == -6

