
class CPU:
    """
    Simulates a basic CPU that executes simple machine instructions stored in memory.
    The CPU has an accumulator for arithmetic operations and a control register (cr) for instruction tracking.
    """
    def __init__(self, memory):
        self.memory: Memory = memory
        self.accumulator: int = 0  # Accumulator
        self.cr: int = 0  # Control register

    def execute(self):
        """
        Executes instructions stored in memory until a HALT instruction (opcode 43) is encountered.
        """
        while True:
            instruction = self.memory.get(self.cr)  # Fetch instruction from memory
            opcode, operand = divmod(instruction, 100)  # Extract opcode and operand

            match opcode:
                # I/O operation
                case 10:  # READ
                    self.read(operand)
                case 11:  # WRITE
                    self.write(operand)

                # Load/store operations
                case 20:  # LOAD
                    self.load(operand)
                case 21:  # STORE
                    self.store(operand)

                # Arithmetic operations
                case 30:  # ADD
                    self.add(operand)
                case 31:  # SUBTRACT
                    self.subtract(operand)
                case 32:  # DIVIDE
                    self.divide(operand)
                case 33:  # MULTIPLY
                    self.multiply(operand)

                # Control operations
                case 40:  # BRANCH
                    self.branch(operand)
                case 41:  # BRANCHNEG
                    self.branchneg(operand)
                case 42:  # BRANCHZERO
                    self.branchzero(operand)
                case 43:  # HALT
                    print("Program halted.")
                    break
                case _:
                    print(f"Unknown opcode: {opcode}. Halting execution.")
                    break
            
            # move to the next memory address
            self.cr += 1

    def read(self, operand):
        while True:
            try:
                value = int(input(f"Enter a value for memory[{operand}]: "))
                self.memory.set(operand, value)
                break  # Exit loop on successful input
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def write(self, operand):
        value = self.memory.get(operand)
        print(f"Value at memory[{operand}]: {value}")

    def load(self, operand):
        self.accumulator = self.memory.get(operand)

    def store(self, operand):
        self.memory.set(operand, self.accumulator)

    def add(self, operand):
        self.accumulator += self.memory.get(operand)

    def subtract(self, operand):
        self.accumulator -= self.memory.get(operand)

    def divide(self, operand):
        divisor = self.memory.get(operand)
        if divisor == 0:
            print("Error: Division by zero. Halting execution.")
            exit(1)
        self.accumulator //= divisor

    def multiply(self, operand):
        self.accumulator *= self.memory.get(operand)

    def branch(self, index):
        """_summary_

        Args:
            index (int): integer specifying where memory should branch
        """
        self.cr = index - 1
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
    """
    Simulates memory with a fixed number of integer storage locations.
    """
    def __init__(self, length=100):
        self.length = length  # Memory size
        self.words = [0] * length  # Initialize memory with zeros

    def get(self, index) -> int:
        """
        Retrieves a value from a specified memory location.
        """
        if 0 <= index < self.length:
            return self.words[index]
        raise IndexError("Memory index out of range")

    def set(self, index: int, value: int):
        """
        Stores a value into a specified memory location.
        """
        if 0 <= index < self.length:
            self.words[index] = value
        else:
            raise IndexError("Memory index out of range")


def main():
    memory = Memory()
    cpu = CPU(memory)

    # Load the program from the file
    try:
        with open('Test1-1.txt', 'r') as program_file:
            instructions = []
            for line in program_file:
                line = line.strip()
                if line and line.lstrip('+-').isdigit():  # Ensure only valid integer lines are processed
                    instructions.append(int(line))
                else:
                    print(f"Warning: Ignoring invalid instruction: {line}")
            for i, instruction in enumerate(instructions):
                memory.set(i, instruction)
    
    except FileNotFoundError:
        print("Error: Program file not found.")
        return
    except ValueError as e:
        print(f"Error reading program: {e}")
        return

    cpu.execute() 

if __name__ == '__main__':
  main()
