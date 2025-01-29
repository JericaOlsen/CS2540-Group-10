class CPU:
  def __init__(self, memory):
    self.accumulator: int = 0

  def execute():
    pass

  def read():
    pass

  def write():
    pass
  def branch(self,index):
    """_summary_

    Args:
        index (int): integer specifying where memory should branch
    """
    self.cr = index
    print("You have branched to location" + str(index))

  def branchneg(self,index):
    """_summary_
      If accumulator is negative branch to a specific location
    """
    if self.accumulator < 0:
      self.branch(index)
    else:
      print("Accumulator isn't negative, there was no branching ")

  def branchzero(self,index):
    """_summary_

      If accumulator is zero branch to a specific location
    """
    if self.accumulator == 0:
      self.branch(index)
    else:
        print("Accumulator isn't zero, there was no branching ")

  
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
