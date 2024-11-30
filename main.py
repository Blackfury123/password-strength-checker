import tkinter as tk
from tkinter import ttk

class PasswordStrengthApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Password Strength Checker")
        self.window.geometry("400x200")

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.password_label = ttk.Label(self.window, text="Password:")
        self.password_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.password_entry = ttk.Entry(self.window, width=20)
        self.password_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.strength_label = ttk.Label(self.window, text="Strength:")
        self.strength_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.strength_value = ttk.Label(self.window, text="Weak", relief="sunken")
        self.strength_value.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.check_button = ttk.Button(self.window, text="Check", command=self.check_strength)
        self.check_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def check_strength(self):
        password = self.password_entry.get()
        strength = self.calculate_strength(password)

        self.strength_value.config(text=f"Strength: {strength}")
        self.strength_value.update_idletasks()

    def calculate_strength(self, password):
        if len(password) < 8:
            return "Weak"
        elif len(password) < 12:
            return "Moderate"
        else:
            return "Strong"

window = tk.Tk()
app = PasswordStrengthApp(window)
window.mainloop()
