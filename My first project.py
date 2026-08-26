from tkinter import *

# Create main window
root = Tk()
root.title("To-Do List")
root.geometry("400x600")
root.config(bg="lightblue")

# Functions to add and delete tasks
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

# Label
label = Label(root, text="My To-Do List", bg="lightblue", font=("Arial", 16, "bold"))
label.pack(pady=10)

# Entry box
entry = Entry(root, width=25, font=("Arial", 14))
entry.pack(pady=10)

# Buttons
add_button = Button(root, text="Add Task", command=add_task, bg="green", fg="white", font=("Arial", 12))
add_button.pack(pady=5)

delete_button = Button(root, text="Delete Task", command=delete_task, bg="red", fg="white", font=("Arial", 12))
delete_button.pack(pady=5)

# Listbox to display tasks
listbox = Listbox(root, width=30, height=15, font=("Arial", 12))
listbox.pack(pady=20)

# Run the GUI loop
root.mainloop()
