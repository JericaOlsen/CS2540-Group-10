import computer
from io import StringIO

def test_student12(monkeypatch):
    inst = [+1007, +1008, + 1009, +3007, +3108, +3009, +4300]

    memory = main.Memory()
    cpu = main.CPU(memory)

    for i, inst in enumerate(inst):
        memory.set(i, inst)

    monkeypatch.setattr('sys.stdin', StringIO("4\n10\n12\n"))

    #User inputs 10 then 7 then 2
    cpu.execute()
    assert cpu.accumulator == 6
