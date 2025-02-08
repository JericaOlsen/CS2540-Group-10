from io import StringIO
from main import Memory, CPU


def test_id6_1(monkeypatch):
    """
        Test input
    """
    memory = Memory()
    cpu = CPU(memory)

    for i, instruction in enumerate([1050, 1051, 2050, 3151, 4206, 1152, 4300]):
        memory.set(i, instruction)

    monkeypatch.setattr('sys.stdin', StringIO("5\n5\n"))
    cpu.execute()

    assert memory.get(50) == 5
    assert memory.get(51) == 5
