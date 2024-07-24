import tkinter as tk
from tkinter import messagebox
tasks={}

def add():
    description=description_entry.get()
    if description:
        number=max(tasks.keys(),default=0)+1
        listbox.insert(tk.END,f"Task {number}: {description}")
        tasks[number]=description
        description_entry.delete(0,tk.END)
    else:
        messagebox.showerror("Error","Please enter task description",parent=root)
def update():
    index=listbox.curselection() #returns index of currently selceted item
    if index:
        index=index[0]
        number=int(listbox.get(index).split(":")[0].split()[1])
        description=description_entry.get()
        if description:
            listbox.delete(index) 
            listbox.insert(index,f"Task {number}: {description}")
            tasks[number]=description
            description_entry.delete(0,tk.END)
        else:
            messagebox.showerror("Error","Please enter task description",parent=root)
    else:
        messagebox.showerror("Error","Please select a task to update",parent=root)    
def delete():
    index=listbox.curselection() #returns index of currently selceted item
    if index:
        index=index[0]
        number=int(listbox.get(index).split(":")[0].split()[1])
        del tasks[number]
        listbox.delete(index)
        rearrange_numbers()
    else:
        messagebox.showerror("Error","Please select a task to delete",parent=root)
def rearrange_numbers():
    number=list(tasks.keys())
    number.sort()
    for i,number in enumerate(number):
        description=tasks[number]
        listbox.delete(i)
        listbox.insert(i,f"Task {i+1}: {description}")
        tasks[i+1]=description
        del tasks[number]
root=tk.Tk()
root.title("To-Do List")
root.config(background="purple")
tk.Label(root,text="Task Description:",bg="purple",fg="white").pack()
description_entry=tk.Entry(root,width=50,bg="white",fg="black")
description_entry.pack()
tk.Button(root,text="Add Task",command=add,bg="green",fg="white").pack()
tk.Button(root,text="Update Task",command=update,bg="yellow",fg="black").pack()
tk.Button(root,text="Delete Task",command=delete,bg="crimson",fg="white").pack()
listbox=tk.Listbox(root,width=50,bg="white",fg="black")
listbox.pack()
root.mainloop()