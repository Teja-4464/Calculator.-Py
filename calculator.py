

import tkinter as tk
def calculate():
    try:
        num1=float(entry_num1.get())
        num2=float(entry_num2.get())
        operation = operation_var.get()
        if operation =="+":
            result = num1 + num2
        elif operation =="-":
            result = num1 - num2
        elif operation =="*":
            result = num1 * num2
        elif operation =="/":
            if num2 !=0:
                result = num1 / num2
            else:
                result_label.config(text="cannot divide by zero")
                return
        else:
            result_label.config(text="invalid operation")
            return

        result_label.config(text="Result:" + str(result))
    except ValueError:
        result_label.config(text="Invalid input")
def clear_fields():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    operation_var.set("+")
    result_label.config(text="Result:")

window=tk.Tk()
window.title("simple calculator")

entry_num1=tk.Entry(window)
entry_num1.grid(row=0,column=0,padx=10,pady=10)

entry_num2=tk.Entry(window)
entry_num2.grid(row=1,column=0,padx=10,pady=10)

operations=["+","-","*","/"]
operation_var=tk.StringVar()
operation_var.set("select")
operation_menu=tk.OptionMenu(window,operation_var,*operations)
operation_menu.grid(row=0,column=2,padx=10,pady=10)

calculate_button=tk.Button(window,text="calculate",command=calculate)
calculate_button.grid(row=2,column=0,columnspan=3,pady=10)

result_label=tk.Label(window,text="Result:",bg="lightgreen")
result_label.grid(row=3,column=0,columnspan=3,pady=10)

clear_button = tk.Button(window, text="Clear", command=clear_fields, bg="orange", fg="white")
clear_button.grid(row=4, column=1, pady=10)

window.mainloop()
