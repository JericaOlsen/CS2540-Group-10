class CPU:
  def __init__(self, memory):
    self.accumulator: int = 0

  def execute():
    pass

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
