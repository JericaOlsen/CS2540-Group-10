import computer
from io import StringIO

def test_teacher72(monkeypatch):
    inst = [+1060, +1061, +1062, +1063, +2060, +3361, +3362, +3363, +2164, +1164, +4300]

    memory = computer.Memory()
    cpu = computer.CPU(memory)

    for i, inst in enumerate(inst):
        memory.set(i, inst)

    monkeypatch.setattr('sys.stdin', StringIO("24\n24\n24\n24\n"))
    #User inputs 24 four times
    cpu.execute()
    assert cpu.accumulator == 331776 
