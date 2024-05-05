import tkinter as tk

def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        result.set("Error")

def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        result.set("Error")

def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        result.set("Error")

def divide():
    try:
        if float(num2.get()) == 0:
            result.set("Error! Division by zero")
        else:
            result.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        result.set("Error")

def clear():
    num1.set("")
    num2.set("")
    result.set("")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Variables to store input and result
num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

# Entry widgets for numbers and result
tk.Label(root, text="Enter first number:").grid(row=0, column=0)
tk.Entry(root, textvariable=num1).grid(row=0, column=1)
tk.Label(root, text="Enter second number:").grid(row=1, column=0)
tk.Entry(root, textvariable=num2).grid(row=1, column=1)
tk.Label(root, text="Result:").grid(row=2, column=0)
tk.Entry(root, textvariable=result, state='readonly').grid(row=2, column=1)

# Buttons for arithmetic operations
tk.Button(root, text="Add", command=add).grid(row=3, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=3, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=4, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=4, column=1)

# Button to clear input fields
tk.Button(root, text="Clear", command=clear).grid(row=5, columnspan=2)

root.mainloop()
