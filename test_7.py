import main

def test_teacher7():
    inst = [+1060, +1061, +1062, +1063, +2060, +3361, +3362, +3363, +2164, +1164, +4300]

    memory = main.Memory()
    cpu = main.CPU(memory)

    for i, inst in enumerate(inst):
        memory.set(i, inst)

    #User inputs 3 four times
    cpu.execute()
    assert cpu.accumulator == 81    

def test_teacher72():
    inst = [+1060, +1061, +1062, +1063, +2060, +3361, +3362, +3363, +2164, +1164, +4300]

    memory = main.Memory()
    cpu = main.CPU(memory)

    for i, inst in enumerate(inst):
        memory.set(i, inst)

    #User inputs 24 four times
    cpu.execute()
    assert cpu.accumulator == 331776 
