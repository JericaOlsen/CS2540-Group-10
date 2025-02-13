import main
from io import StringIO


def test_student1(monkeypatch):
    inst = [+1007, +1008, + 1009, +3007, +3108, +3009, +4300]

    memory = main.Memory()
    cpu = main.CPU(memory)

    for i, inst in enumerate(inst):
        memory.set(i, inst)

    monkeypatch.setattr('sys.stdin', StringIO("28\n5\n4\n"))


    #User inputs 28 then 5 then 4
    cpu.execute()
    assert cpu.accumulator == 27
    

    
