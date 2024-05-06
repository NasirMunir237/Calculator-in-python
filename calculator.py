import tkinter as tk

# Function to update the display when a button is clicked
def button_click(symbol):
    current = display_var.get()
    if current == "Error":
        current = ""
    if symbol == "=":
        try:
            result = str(eval(current))
        except:
            result = "Error"
        display_var.set(result)
    elif symbol == "C":
        display_var.set("")
    else:
        display_var.set(current + symbol)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a variable to hold the display value
display_var = tk.StringVar()
display_var.set("")

# Create the display
display = tk.Entry(root, textvariable=display_var, font=("Arial", 18), bd=10, insertwidth=4, width=15, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Define button symbols
button_symbols = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Create buttons
for symbol, row, column in button_symbols:
    button = tk.Button(root, text=symbol, font=("Arial", 18), padx=20, pady=20, command=lambda sym=symbol: button_click(sym))
    button.grid(row=row, column=column)

# Run the main loop
root.mainloop()
