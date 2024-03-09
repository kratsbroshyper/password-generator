import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Modern Password Generator")

        self.label = tk.Label(master, text="Password Length:")
        self.label.pack()

        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="")
        self.password_label.pack()

    def generate_password(self):
        length = self.length_entry.get()
        if not length.isdigit():
            messagebox.showerror("Error", "Please enter a valid length.")
            return

        length = int(length)
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.password_label.config(text=password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
