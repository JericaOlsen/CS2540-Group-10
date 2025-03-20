import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox, simpledialog
from computer import Memory, CPU


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.instructions = []  # Holds program commands as integers
        self.create_widgets()

    def create_widgets(self):
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        load_program_button = tk.Button(button_frame, text="Load Program", command=self.load_program)
        save_program_button = tk.Button(button_frame, text="Save Program", command=self.save_program)
        execute_program_button = tk.Button(button_frame, text="Execute Program", command=self.execute_program)

        load_program_button.pack(side=tk.LEFT)
        save_program_button.pack(side=tk.LEFT)
        execute_program_button.pack(side=tk.LEFT)

        # Text Editor for direct command editing
        self.text_editor = tk.Text(self, width=50, height=20)
        self.text_editor.pack(fill=tk.BOTH, expand=True)

    def load_program(self):
        """Loads a program file and displays its content in the text editor."""
        program_file_name = askopenfilename(title="Select Program File")
        if not program_file_name:
            return
        try:
            with open(program_file_name, 'r') as program_file:
                content = program_file.read()
            self.text_editor.delete("1.0", tk.END)
            self.text_editor.insert("1.0", content)
        except FileNotFoundError:
            messagebox.showerror("Error", "Program file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def save_program(self):
        """Saves the current program from the text editor to a file, with validation."""
        file_path = asksaveasfilename(title="Save Program As", defaultextension=".txt",
                                      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not file_path:
            return

        content = self.text_editor.get("1.0", tk.END).strip()
        lines = content.split("\n")
        validated_instructions = []

        for line in lines:
            line = line.strip()
            if line and line.lstrip('+-').isdigit():
                validated_instructions.append(line)
            else:
                messagebox.showerror("Error", f"Invalid instruction found: '{line}'. Fix it before saving.")
                return

        if len(validated_instructions) > 100:
            messagebox.showerror("Error", "Program exceeds the maximum size of 100 instructions.")
            return

        try:
            with open(file_path, 'w') as f:
                for instr in validated_instructions:
                    f.write(f"{instr}\n")
            messagebox.showinfo("Success", "Program saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save program: {e}")

    def execute_program(self):
        """Loads the current instructions into memory and runs the CPU execution."""
        content = self.text_editor.get("1.0", tk.END).strip()
        lines = content.split("\n")

        try:
            self.instructions = [int(line.strip()) for line in lines if line.strip()]
            if len(self.instructions) > 100:
                messagebox.showerror("Error", "Program exceeds the maximum size of 100 instructions.")
                return

            memory = Memory()
            cpu = CPU(memory, self.open_output_window, self.open_input_window)

            for i, instr in enumerate(self.instructions):
                memory.set(i, instr)

            cpu.execute()
        except ValueError:
            messagebox.showerror("Error", "Program contains invalid instructions. Please check before executing.")
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
