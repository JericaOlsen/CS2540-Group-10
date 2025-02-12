import tkinter as tk
from tkinter import filedialog, scrolledtext


class CPU:
    def __init__(self, memory, output_widget, root):
        self.memory: Memory = memory
        self.accumulator: int = 0
        self.cr: int = 0
        self.output_widget = output_widget  # Redirect output to Tkinter widget
        self.root = root  # Tkinter root for dialogs
        self.is_waiting_for_input = False  # Flag to handle input interruption

    def log(self, message):
        """Log output to the text widget in the GUI."""
        self.output_widget.insert(tk.END, message + "\n")
        self.output_widget.see(tk.END)

    def execute(self):
        """Executes instructions in memory, handling input seamlessly."""
        while not self.is_waiting_for_input:  # Ensure execution continues after input
            instruction = self.memory.get(self.cr)
            opcode, operand = divmod(instruction, 100)

            match opcode:
                case 10:
                    self.read(operand)
                    return  # Stop execution temporarily for input
                case 11:
                    self.write(operand)
                case 20:
                    self.load(operand)
                case 21:
                    self.store(operand)
                case 30:
                    self.add(operand)
                case 31:
                    self.subtract(operand)
                case 32:
                    self.divide(operand)
                case 33:
                    self.multiply(operand)
                case 40:
                    self.branch(operand)
                case 41:
                    self.branchneg(operand)
                case 42:
                    self.branchzero(operand)
                case 43:
                    self.log("Program halted.")
                    return  # Stop execution
                case _:
                    self.log(f"Unknown opcode: {opcode}. Halting execution.")
                    return
            
            self.cr += 1
        self.log("Execution complete.")

    def read(self, operand):
        """Prompts the user for input using a pop-up window and resumes execution."""

        def store_value(event=None):  # Handle both button click and Enter key press
            try:
                value = int(entry.get())
                self.memory.set(operand, value)
                popup.destroy()
                self.is_waiting_for_input = False  # Reset flag
                self.execute()  # Resume execution
            except ValueError:
                self.log("Invalid input. Please enter an integer.")

        self.is_waiting_for_input = True  # Set flag to pause execution
        popup = tk.Toplevel(self.root)
        popup.title("Input Required")

        tk.Label(popup, text=f"Enter a value for memory[{operand}]:").pack(pady=5)
        entry = tk.Entry(popup)
        entry.pack(pady=5)
        entry.focus()

        ok_button = tk.Button(popup, text="OK", command=store_value)
        ok_button.pack(pady=5)

        entry.bind("<Return>", store_value)  # Bind Enter key to submit input
        self.root.wait_window(popup)  # Wait until user provides input

    def write(self, operand):
        """Displays memory value in the GUI output window."""
        value = self.memory.get(operand)
        self.log(f"Value at memory[{operand}]: {value}")

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
            self.log("Error: Division by zero. Halting execution.")
            return
        self.accumulator //= divisor

    def multiply(self, operand):
        self.accumulator *= self.memory.get(operand)

    def branch(self, index):
        self.cr = index - 1
        self.log(f"Branched to location {index}")

    def branchneg(self, index):
        if self.accumulator < 0:
            self.branch(index)
        else:
            self.log("Accumulator isn't negative, no branching occurred")

    def branchzero(self, index):
        if self.accumulator == 0:
            self.branch(index)
        else:
            self.log("Accumulator isn't zero, no branching occurred")


class Memory:
    """Simulates computer memory."""
    def __init__(self, length=100):
        self.length = length
        self.words = [0] * length

    def get(self, index) -> int:
        if 0 <= index < self.length:
            return self.words[index]
        raise IndexError("Memory index out of range")

    def set(self, index: int, value: int):
        if 0 <= index < self.length:
            self.words[index] = value
        else:
            raise IndexError("Memory index out of range")


class CPU_Simulator_GUI:
    """GUI interface for the CPU Simulator."""
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Simulator")

        self.label = tk.Label(root, text="Load a text file containing CPU instructions:")
        self.label.pack(pady=5)

        self.load_button = tk.Button(root, text="Load File", command=self.load_file)
        self.load_button.pack(pady=5)

        self.run_button = tk.Button(root, text="Run Program", command=self.run_program, state=tk.DISABLED)
        self.run_button.pack(pady=5)

        self.output_text = scrolledtext.ScrolledText(root, width=60, height=20)
        self.output_text.pack(pady=10)

        self.memory = Memory()
        self.cpu = CPU(self.memory, self.output_text, self.root)
        self.instructions = []

    def load_file(self):
        """Loads a program file into memory."""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return

        try:
            with open(file_path, 'r') as program_file:
                self.instructions = []
                for line in program_file:
                    line = line.strip()
                    if line and line.lstrip('+-').isdigit():
                        self.instructions.append(int(line))
                    else:
                        self.output_text.insert(tk.END, f"Warning: Ignoring invalid instruction: {line}\n")

                for i, instruction in enumerate(self.instructions):
                    self.memory.set(i, instruction)

            self.output_text.insert(tk.END, f"File '{file_path}' loaded successfully.\n")
            self.run_button.config(state=tk.NORMAL)

        except FileNotFoundError:
            self.output_text.insert(tk.END, "Error: File not found.\n")
        except ValueError as e:
            self.output_text.insert(tk.END, f"Error reading file: {e}\n")

    def run_program(self):
        """Starts program execution."""
        self.output_text.delete(1.0, tk.END)
        self.cpu.execute()


if __name__ == "__main__":
    root = tk.Tk()
    gui = CPU_Simulator_GUI(root)
    root.mainloop()
