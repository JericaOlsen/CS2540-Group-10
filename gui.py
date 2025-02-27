import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox, simpledialog
from computer import Memory, CPU

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        memory = Memory()
        self.cpu = CPU(memory, self.open_output_window, self.open_input_window)
        self.pack()

        load_program_button = tk.Button(self, text="Load Program", command=self.load_program)
        execute_program_button = tk.Button(self, text="Execute Program", command=self.execute_program)

        load_program_button.pack()
        execute_program_button.pack()



    def reset_cpu_memory(self):
        self.memory = Memory()
        self.cpu= CPU(self.memory, self.open_output_window, self.open_input_window)

    def load_program(self):
        program_file_name = askopenfilename()# Load the program from the file
        try:
            self.reset_cpu_memory()
            with open(program_file_name, 'r') as program_file:
                instructions = []
                for line in program_file:
                    line = line.strip()
                    if line and line.lstrip('+-').isdigit():  # Ensure only valid integer lines are processed
                        instructions.append(int(line))
                    else:
                        print(f"Warning: Ignoring invalid instruction: {line}")
                for i, instruction in enumerate(instructions):
                    self.cpu.memory.set(i, instruction)

        except FileNotFoundError:
            self.open_output_window("Error: Program file not found.")
            return
        except ValueError as e:
            self.open_output_window(f"Error reading program: {e}")
            return

    def execute_program(self):
        self.cpu.execute()
        

    def open_output_window(self,output):
        messagebox.showinfo("Output", output)

    def open_input_window(self, input):
        user_input = simpledialog.askstring("Input", input)

        return user_input
      
