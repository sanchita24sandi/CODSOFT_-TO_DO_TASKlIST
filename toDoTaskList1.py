import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to update the task list
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to update a selected task
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            tasks[selected_task_index] = new_task
            update_task_list()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")

# Create GUI components
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

update_task_button = tk.Button(root, text="Update Task", command=update_task)
update_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=35, height=15)
task_listbox.pack(pady=10)

terminate_button = tk.Button(root, text="Terminate", command=root.destroy)
terminate_button.pack(pady=5)

# Run the main application loop
root.mainloop()
