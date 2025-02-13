import computer
from io import StringIO


def test_student4(monkeypatch):
    inst = [+1021, +1033, +1027, +4005, +1028, +2027, +3321, +2122, +1122, +4300]

    memory = computer.Memory()
    cpu = computer.CPU(memory)

    for i, inst in enumerate(inst):
        memory.set(i, inst)
        
    monkeypatch.setattr('sys.stdin', StringIO("12\n4\n7\n"))

    #User inputs 12 then 4 then 7
    cpu.execute()
    assert cpu.accumulator == 84

