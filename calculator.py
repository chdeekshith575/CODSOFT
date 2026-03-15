# simple calculator
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("calculator")
root.geometry("300x400")

num1 = tk.Entry(root, width=20)
num1.pack(pady=10)

num2 = tk.Entry(root, width=20)
num2.pack(pady=10)

op = tk.Entry(root, width=20)
op.pack(pady=10)

result_label = tk.Label(root, text="Result : ")
result_label.pack(pady=10)


def operation(n1, n2, user):
    if user == "+":
        return n1 + n2
    elif user == "-":
        return n1 - n2
    elif user == "*":
        return n1 * n2
    elif user == "/":
        return n1 / n2
    elif user == "%":
        return n1 % n2
    elif user == "//":
        return n1 // n2
    else:
        return "syntax error"


def calculate():
    try:
        n1 = int(num1.get())
        n2 = int(num2.get())
        user = op.get()

        result = operation(n1, n2, user)
        result_label.config(text="Result : " + str(result))

    except:
        messagebox.showerror("Error", "Please enter valid numbers")


btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack(pady=20)

root.mainloop()