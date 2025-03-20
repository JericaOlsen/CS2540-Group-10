import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter import messagebox, simpledialog
from computer import Memory, CPU
import configparser

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        memory = Memory()
        self.cpu = CPU(memory, self.open_output_window, self.open_input_window)
        self.pack()

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        menubar = tk.Menu(master)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Load Program", command=self.load_program)
        file_menu.add_command(label="Save Program", command=self.save_program) # save_program still needs to be implemented
        menubar.add_cascade(label="File", menu=file_menu)

        colors_menu = tk.Menu(menubar, tearoff=0)
        colors_menu.add_command(label="Select Window Foreground", command=self.select_window_foreground)
        colors_menu.add_command(label="Select Window Background", command=self.select_window_background)
        colors_menu.add_command(label="Select Button Foreground", command=self.select_button_foreground)
        colors_menu.add_command(label="Select Button Background", command=self.select_button_background)
        menubar.add_cascade(label="Colors", menu=colors_menu)

        self.master.config(menu=menubar)


        self.master.option_add('*foreground', self.config['window']['foreground'])
        self.master.option_add('*background', self.config['window']['background'])
        self.master.option_add('*Button.foreground', self.config['button']['foreground'])
        self.master.option_add('*Button.background', self.config['button']['background'])

        #load_program_button = tk.Button(self, text="Load Program", command=self.load_program)
        execute_program_button = tk.Button(self, text="Execute Program", command=self.execute_program)

        #load_program_button.pack()
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

    def save_program(self):
        pass

    def execute_program(self):
        self.cpu.execute()
        

    def open_output_window(self, output):
        # Close any existing output window
        if hasattr(self, 'output_window') and self.output_window.winfo_exists():
            self.output_window.destroy()

        self.output_window = tk.Toplevel(self)
        self.output_window.title("Output")

        label = tk.Label(self.output_window, text=output, fg="#333333", bg="#f0f0f0")  # Text and background color
        label.pack(padx=20, pady=10)

        close_button = tk.Button(self.output_window, text="Close", command=self.output_window.destroy)    
        close_button.pack(pady=5)

    def open_input_window(self, prompt):
        # Close any existing input window
        if hasattr(self, 'input_window') and self.input_window.winfo_exists():
            self.input_window.destroy()

        self.input_window = tk.Toplevel(self)
        self.input_window.title("Input")

        label = tk.Label(self.input_window, text=prompt)
        label.pack(padx=20, pady=10)

        input_value = tk.StringVar()
        input_entry = tk.Entry(self.input_window, textvariable=input_value)
        input_entry.pack(pady=5)
        input_entry.focus_set()

         # Handle input submission
        def on_submit():
            self.user_input = input_value.get()
            self.input_window.destroy()

        submit_button = tk.Button(self.input_window, text="Submit",
                              command=on_submit)  # Button color
        submit_button.pack(pady=5)

        # Wait until the window is closed
        self.input_window.wait_window()

        # Return user input after window is closed
        return self.user_input


    def select_window_foreground(self):
        self.config['window']['foreground'] = askcolor()[1] or self.config['window']['foreground']

        with open('config.ini', 'w') as config_file:
            self.config.write(config_file)
    
        self.master.option_add('*foreground', self.config['window']['foreground'])

    def select_window_background(self):
        self.config['window']['background'] = askcolor()[1] or self.config['window']['background']

        with open('config.ini', 'w') as config_file:
            self.config.write(config_file)
    
        self.master.option_add('*background', self.config['window']['background'])

    def select_button_foreground(self):
        self.config['button']['foreground'] = askcolor()[1] or self.config['button']['foreground']

        with open('config.ini', 'w') as config_file:
            self.config.write(config_file)
    
        self.master.option_add('*Button.foreground', self.config['button']['foreground'])

    def select_button_background(self):
        self.config['button']['background'] = askcolor()[1] or self.config['button']['foreground']

        with open('config.ini', 'w') as config_file:
            self.config.write(config_file)
    
        self.master.option_add('*Button.background', self.config['button']['background'])
