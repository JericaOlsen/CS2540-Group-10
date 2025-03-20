import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox, simpledialog
from computer import Memory, CPU

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.instructions = []  # Holds program commands as integers
        self.clipboard = None   # For cut/copy/paste operations
        self.create_widgets()

    def create_widgets(self):
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        load_program_button = tk.Button(button_frame, text="Load Program", command=self.load_program)
        save_program_button = tk.Button(button_frame, text="Save Program", command=self.save_program)
        execute_program_button = tk.Button(button_frame, text="Execute Program", command=self.execute_program)
        add_button = tk.Button(button_frame, text="Add", command=self.add_instruction)
        modify_button = tk.Button(button_frame, text="Modify", command=self.modify_instruction)
        delete_button = tk.Button(button_frame, text="Delete", command=self.delete_instruction)
        cut_button = tk.Button(button_frame, text="Cut", command=self.cut_instruction)
        copy_button = tk.Button(button_frame, text="Copy", command=self.copy_instruction)
        paste_button = tk.Button(button_frame, text="Paste", command=self.paste_instruction)

        # Pack the buttons in the frame
        load_program_button.pack(side=tk.LEFT)
        save_program_button.pack(side=tk.LEFT)
        execute_program_button.pack(side=tk.LEFT)
        add_button.pack(side=tk.LEFT)
        modify_button.pack(side=tk.LEFT)
        delete_button.pack(side=tk.LEFT)
        cut_button.pack(side=tk.LEFT)
        copy_button.pack(side=tk.LEFT)
        paste_button.pack(side=tk.LEFT)

        # Listbox to display and inspect program commands
        self.listbox = tk.Listbox(self, width=50)
        self.listbox.pack(fill=tk.BOTH, expand=True)

    def refresh_listbox(self):
        """Updates the listbox to display current instructions with indices."""
        self.listbox.delete(0, tk.END)
        for idx, instr in enumerate(self.instructions):
            self.listbox.insert(tk.END, f"#{idx:02d}: {instr}")

    def load_program(self):
        """Loads a program file from a user-specified folder and displays its commands."""
        program_file_name = askopenfilename(title="Select Program File")
        if not program_file_name:
            return
        try:
            with open(program_file_name, 'r') as program_file:
                new_instructions = []
                for line in program_file:
                    line = line.strip()
                    if line and line.lstrip('+-').isdigit():
                        new_instructions.append(int(line))
                    else:
                        print(f"Warning: Ignoring invalid instruction: {line}")
                if len(new_instructions) > 100:
                    messagebox.showerror("Error", "Program exceeds maximum size of 100 instructions.")
                    return
                self.instructions = new_instructions
                self.refresh_listbox()
        except FileNotFoundError:
            messagebox.showerror("Error", "Program file not found.")
        except ValueError as e:
            messagebox.showerror("Error", f"Error reading program: {e}")

    def save_program(self):
        """Saves the current program to a file in a user-specified folder."""
        if not self.instructions:
            messagebox.showinfo("Info", "No program loaded to save.")
            return
        file_path = asksaveasfilename(title="Save Program As", defaultextension=".txt",
                                      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not file_path:
            return
        try:
            with open(file_path, 'w') as f:
                for instr in self.instructions:
                    f.write(f"{instr}\n")
            messagebox.showinfo("Success", "Program saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save program: {e}")

    def add_instruction(self):
        """Adds a new instruction to the program (if under the 100-instruction limit)."""
        if len(self.instructions) >= 100:
            messagebox.showerror("Error", "Cannot add instruction. Maximum size reached.")
            return
        new_instr = simpledialog.askstring("Add Instruction", "Enter new instruction (integer):")
        if new_instr is None:
            return
        if new_instr.lstrip('+-').isdigit():
            self.instructions.append(int(new_instr))
            self.refresh_listbox()
        else:
            messagebox.showerror("Error", "Invalid instruction. Must be an integer.")

    def modify_instruction(self):
        """Modifies the selected instruction."""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Info", "No instruction selected.")
            return
        index = selected[0]
        current_value = self.instructions[index]
        new_value = simpledialog.askstring("Modify Instruction", 
                                           f"Current value is {current_value}. Enter new instruction (integer):")
        if new_value is None:
            return
        if new_value.lstrip('+-').isdigit():
            self.instructions[index] = int(new_value)
            self.refresh_listbox()
        else:
            messagebox.showerror("Error", "Invalid instruction. Must be an integer.")

    def delete_instruction(self):
        """Deletes the selected instruction."""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Info", "No instruction selected.")
            return
        index = selected[0]
        del self.instructions[index]
        self.refresh_listbox()

    def cut_instruction(self):
        """Cuts the selected instruction to the clipboard and removes it from the program."""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Info", "No instruction selected.")
            return
        index = selected[0]
        self.clipboard = self.instructions[index]
        del self.instructions[index]
        self.refresh_listbox()

    def copy_instruction(self):
        """Copies the selected instruction to the clipboard."""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Info", "No instruction selected.")
            return
        index = selected[0]
        self.clipboard = self.instructions[index]

    def paste_instruction(self):
        """Pastes the instruction from the clipboard at the selected position if size allows."""
        if self.clipboard is None:
            messagebox.showinfo("Info", "Clipboard is empty.")
            return
        if len(self.instructions) >= 100:
            messagebox.showerror("Error", "Cannot paste instruction. Maximum size reached.")
            return
        # Insert at the selected index or at the end if nothing is selected
        selected = self.listbox.curselection()
        index = selected[0] if selected else len(self.instructions)
        self.instructions.insert(index, self.clipboard)
        self.refresh_listbox()

    def execute_program(self):
        """Loads the current instructions into memory and runs the CPU execution."""
        if not self.instructions:
            messagebox.showinfo("Info", "No program loaded to execute.")
            return
        try:
            memory = Memory()
            cpu = CPU(memory, self.open_output_window, self.open_input_window)
            for i, instr in enumerate(self.instructions):
                memory.set(i, instr)
            cpu.execute()
        except Exception as e:
            messagebox.showerror("Execution Error", f"An error occurred during execution: {e}")

    def open_output_window(self, output):
        """Displays output messages."""
        messagebox.showinfo("Output", output)

    def open_input_window(self, prompt):
        """Prompts the user for input during execution."""
        return simpledialog.askstring("Input", prompt)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Program Editor")
    app = MainWindow(root)
    root.mainloop()
