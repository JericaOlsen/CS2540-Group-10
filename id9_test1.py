from computer import Memory, CPU

def test_id9_1(capsys):
    memory = Memory()
    cpu = CPU(memory, print, input)

    for i, instruction in enumerate([1100, 1101, 1102, 4300]):
        memory.set(i, instruction)
    cpu.execute()

    assert capsys.readouterr().out == "Value at memory[0]: 1100\n"\
                                      "Value at memory[1]: 1101\n"\
                                      "Value at memory[2]: 1102\n"\
                                      "Program halted.\n"
