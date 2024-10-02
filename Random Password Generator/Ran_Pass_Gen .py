import tkinter as tk
from tkinter import ttk
import string
import secrets

# Define the PasswordGeneratorGUI 
class PasswordGeneratorGUI:
    def __init__(self):
        # Initialize the main window
        self.window = tk.Tk()
        self.window.title("Random Password Generator")

        self.input_frame = ttk.Frame(self.window)
        self.input_frame.pack(padx=10, pady=10)

        self.length_label = ttk.Label(self.input_frame, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5)
        self.length_entry = ttk.Entry(self.input_frame, width=5) 
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)

        self.complexity_frame = ttk.Frame(self.input_frame)
        self.complexity_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.use_uppercase = tk.BooleanVar()  
        self.use_uppercase_check = ttk.Checkbutton(self.complexity_frame, text="Uppercase", variable=self.use_uppercase)
        self.use_uppercase_check.pack(side=tk.LEFT)

        self.use_numbers = tk.BooleanVar() 
        self.use_numbers_check = ttk.Checkbutton(self.complexity_frame, text="Numbers", variable=self.use_numbers)
        self.use_numbers_check.pack(side=tk.LEFT)

        self.use_punctuation = tk.BooleanVar()  
        self.use_punctuation_check = ttk.Checkbutton(self.complexity_frame, text="Punctuation", variable=self.use_punctuation)
        self.use_punctuation_check.pack(side=tk.LEFT)

        self.generate_button = ttk.Button(self.window, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(padx=10, pady=10)

        self.output_label = ttk.Label(self.window, text="")
        self.output_label.pack(padx=10, pady=10)

    # Method to generate a random password based on user input
    def generate_password(self):
        length = int(self.length_entry.get())

        characters = string.ascii_lowercase

        if self.use_uppercase.get():
            characters += string.ascii_uppercase

        if self.use_numbers.get():
            characters += string.digits

        if self.use_punctuation.get():
            characters += string.punctuation

        password = ''.join(secrets.choice(characters) for _ in range(length))
        self.output_label.config(text=f"Generated Password: {password}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = PasswordGeneratorGUI() 
    gui.run()  
