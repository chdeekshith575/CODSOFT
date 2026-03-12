import tkinter as tk
from tkinter import messagebox

# Function to add task
def addTask():
    t = task_entry.get()
    if t != "":
        listbox_tasks.insert(tk.END, t)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", " enter some task first!") 

# Function to delete task
def deleteTask():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Error", "Please select any task to delete.")

# Function to clear list
def clearList():
    listbox_tasks.delete(0, tk.END)

# Main UI setup
root = tk.Tk()
root.title("My To-Do List App")
root.geometry("350x400")

# Title inside the app
label = tk.Label(root, text="Work to be done", font=("Arial", 12, "bold"))
label.pack(pady=10)

# Entry box to type tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

# Buttons - simple colors
add_button = tk.Button(root, text="Add", width=20, command=addTask, bg="lightblue")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete", width=20, command=deleteTask, bg="orange")
delete_button.pack(pady=5)

# Listbox to show tasks
listbox_tasks = tk.Listbox(root, height=10, width=40)
listbox_tasks.pack(pady=10)

clear_button = tk.Button(root, text="Clear Everything", width=20, command=clearList, bg="yellow")
clear_button.pack(pady=5)

root.mainloop()