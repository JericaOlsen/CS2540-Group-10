from math import divmod

class CPU:
  def __init__(self, memory):
    self.memory: Memory = memory
    self.accumulator: int = 0
    self.cr: int = 0

  def execute(instructions):

    for i in range(self.memory.length):
      self.memory.put(i, instructions[i])

      self.cr = 0
    while True:
      instruction = self.memory(self.cr)
      opcode, operand = divmod(instruction, 200)


      match opcode:
        case 10:
          read(operand)
        case 11:
          write(operand)
        case 20:
          load(operand)
        case 43:
          break
      self.cr += 1

  def read():
    pass

  def write():
    pass

class Memory:
  def __init__(self, legnth = 100):
    self.length = length
    self.words = []

def get(index) -> int:
  pass

def set(index: int, value: int)

def main(args):
  memory = Memory()
  cpu = CPU(memory)

  with open(args[1], 'w') as program_file:
    instructions = []
    for line in program_file.readlines():
      instructions.append(int(line))

    cpu.execute(instructions)

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
