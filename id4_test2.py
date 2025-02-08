import main

def test_student41():
    inst = [+1021, +1033, +1027, +4006, +1028, +2027, +3321, +2122, +1122, +4300]

    memory = main.Memory()
    cpu = main.CPU(memory)

    for i, inst in enumerate(inst):
        memory.set(i, inst)

    #User inputs 12 then 4 then 7
    cpu.execute()
    assert cpu.accumulator == 0
