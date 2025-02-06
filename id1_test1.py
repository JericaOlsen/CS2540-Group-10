import main

def test_student1():
    inst = [+1007, +1008, + 1009, +3007, +3108, +3009, +4300]

    memory = main.Memory()
    cpu = main.CPU(memory)

    for i, inst in enumerate(inst):
        memory.set(i, inst)

    #User inputs 28 then 5 then 4
    cpu.execute()
    assert cpu.accumulator == 27
    

    
