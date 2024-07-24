import tkinter as tk

def cal():
    num1=float(entry_num1.get())
    num2=float(entry_num2.get())
    operation=operation_var.get()
    if operation=="+":
        result=num1+num2
    elif operation=="-":
        result=num1-num2
    elif operation=="*":
        result=num1*num2
    elif operation=="/":
        if num2!=0:
            result=num1/num2
        else:
            result="Error: Division by zero"
    l_result.config(text="Result: " + str(result))

def clear():
    entry_num1.delete(0,tk.END)
    entry_num2.delete(0,tk.END)
    l_result.config(text="Result: ")

root=tk.Tk()
root.title("Simple Calculator")
root.geometry("450x400")

l_num1=tk.Label(root,text="Number 1: ")
l_num1.grid(row=0,column=0,padx=10,pady=10)
entry_num1=tk.Entry(root,width=20)
entry_num1.grid(row=0,column=1,padx=10,pady=10)
l_num2=tk.Label(root,text="Number 2: ")
l_num2.grid(row=1,column=0,padx=10,pady=10)
entry_num2=tk.Entry(root,width=20)
entry_num2.grid(row=1,column=1,padx=10,pady=10)

operation_var=tk.StringVar()
operation_var.set("+")

r_add=tk.Radiobutton(root,text="+",variable=operation_var,value="+")
r_add.grid(row=2, column=0,padx=10,pady=10)
r_sub=tk.Radiobutton(root,text="-",variable=operation_var,value="-")
r_sub.grid(row=2, column=1,padx=10,pady=10)
r_mul=tk.Radiobutton(root,text="*",variable=operation_var,value="*")
r_mul.grid(row=2, column=2,padx=10,pady=10)
r_div=tk.Radiobutton(root,text="/",variable=operation_var,value="/")
r_div.grid(row=2, column=3,padx=10,pady=10)

b_calculator=tk.Button(root,text="Calculate",command=cal)
b_calculator.grid(row=3,column=1,padx=10,pady=10)
b_clear=tk.Button(root,text="Clear",command=clear)
b_clear.grid(row=4,column=1,padx=10,pady=10)

l_result=tk.Label(root,text="Result: ")
l_result.grid(row=5,column=1,padx=10,pady=10)
root.mainloop()