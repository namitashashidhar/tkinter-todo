import tkinter as tk
from tkinter import ttk

COMPARTMENT_COLORS = {
    "Collins": "#9c6bdb",  # purple
    "Coding": "#369c56",  # green
    "Research": "#7a9ccf",  # indigo
    "Fun": "#c78fdb", # pink
    "Other": "#bebabf",  # gray
    "Calc 3": "#e8b261" #orangeish
}

def add_task():
    task = entry.get()
    compartment = compartment_var.get()
    if task and compartment:
        listbox.insert("", tk.END, values=(compartment, task), tags=(compartment,))
        entry.delete(0, tk.END)

def delete_task():
    try:
        selection = listbox.selection()
        listbox.delete(selection)
    except:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

style = ttk.Style()
style.configure("Treeview", font=("Courier New", 12))
style.configure("Treeview.Heading", font=("Courier New", 12, "bold"))

listbox = ttk.Treeview(
    frame,
    columns=("compartment", "task"),
    show="headings",
    selectmode="browse",
)
listbox.column("compartment", width=150, anchor="center")
listbox.column("task", width=300, anchor="w")

listbox.heading("compartment", text="Compartment")
listbox.heading("task", text="Task")

for compartment, color in COMPARTMENT_COLORS.items():
    style.configure(f"{compartment}.Treeview", background=color)

    listbox.tag_configure(compartment, background=color, foreground="black")

listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(
    root,
    font=("Courier New", 12)
)
entry.pack(pady=10)

compartment_var = tk.StringVar(root)
compartment_var.set("Work")  # Default compartment

compartment_menu = tk.OptionMenu(
    root,
    compartment_var,
    *COMPARTMENT_COLORS.keys(),
)
compartment_menu.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    command=add_task,
    font=("Courier New", 12),
)
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    command=delete_task,
    font=("Courier New", 12),
)
delete_button.pack(side=tk.LEFT)

root.mainloop()
