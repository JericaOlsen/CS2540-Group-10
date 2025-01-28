class Memory:
  def __init__(self, length: int = 100):
    self.length: int = length
    self.words: list[int] = [0 for _ in range(length)]

  def get(self, address: int) -> int:
    if address >= self.length:
      raise IndexError

    return self.words[address]

  def set(self, address: int, value: int) -> None:
    if address >= self.length:
      raise IndexError

    self.words[address] = value


class CPU:
  def __init__(self, memory: Memory):
    self.memory: Memory = memory
    self.accumulator: int = 0
    self.cr: int = 0

  def execute(self, instructions: list[int]):
    # load instructions into memory
    for i in range(min(self.memory.length, len(instructions))):
      self.memory.set(i, instructions[i])

    # start at the beginning
    self.cr = 0

    # execute the instructions
    while True:
      instruction = self.memory.get(self.cr)

      opcode, operand = divmod(instruction, 100)

      match opcode:
        # I/O operation
        case 10:
          self.read(operand)
        case 11:
          self.write(operand)

        # Load/store operations
        case 20:
          self.load(operand)
        case 21:
          self.store(operand)

        # Arithmetic operations
        case 30:
          self.add(operand)
        case 31:
          self.subtract(operand)
        case 32:
          self.divide(operand)
        case 33:
          self.multiply(operand)

        # Control operation
        case 40:
          self.branch(operand)
        case 41:
          self.branchneg(operand)
        case 42:
          self.branchzero(operand)
        case 43:
          break

      # move to the next memory address
      self.cr += 1

      # stop at end
      if self.cr >= self.memory.length:
        break

  # I/O operation
  def read(self, address: int) -> None:
    word = int(input())
    self.memory.set(address, word)

  def write(self, address: int) -> None:
    print(self.memory.get(address))

  # Load/store operations
  def load(self, address: int) -> None:
    self.accumulator = self.memory.get(address)

  def store(self, address: int) -> None:
    self.memory.set(address, self.accumulator)

  # Arithmetic operations
  def add(self, address: int) -> None:
    pass

  def subtract(self, address: int) -> None:
    pass

  def divide(self, address: int) -> None:
    pass

  def multiply(self, address: int) -> None:
    pass

  # Control operation
  def branch(self, address: int) -> None:
    pass

  def branchneg(self, address: int) -> None:
    pass

  def branchzero(self, address: int) -> None:
    pass


def main(args: list[str]) -> None:
  # initialize memory and cpu
  memory: Memory = Memory()
  cpu: CPU = CPU(memory)

  # read program file
  instructions: list[int] = []
  with open(args[1], 'r') as program_file:
    for line in program_file:
      instructions.append(int(line))

  # execute instructions
  cpu.execute(instructions)

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
