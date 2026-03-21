import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        # Get length from user input
        length = int(length_entry.get())
        
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4 for better security.")
            return

        # Define character sets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Combine all characters
        all_chars = lower + upper + digits + symbols

        # Generate random password
        password = "".join(random.sample(all_chars, length))
        
        # Display the password in the result entry
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

# --- UI Setup ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")

# Label
tk.Label(root, text="Enter Password Length:", font=("Arial", 10)).pack(pady=10)

# Entry for length
length_entry = tk.Entry(root, font=("Arial", 12), width=10)
length_entry.pack(pady=5)

# Button to generate
gen_btn = tk.Button(root, text="Generate Password", bg="lightblue", command=generate_password)
gen_btn.pack(pady=20)

# Result Label and Entry
tk.Label(root, text="Your Generated Password:", font=("Arial", 10)).pack(pady=5)
result_entry = tk.Entry(root, font=("Arial", 12, "bold"), width=25, justify="center")
result_entry.pack(pady=5)

root.mainloop()