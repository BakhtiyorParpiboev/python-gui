from tkinter import *
from math import *

def calculate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

def insert_text(text):
    current_text = entry.get()
    entry.delete(0, END)
    entry.insert(END, current_text + text)

root = Tk()
root.geometry("400x500")
root.title("My First GUI Calculator")

entry = Entry(root, font=("arial", 24), borderwidth=2, relief="solid", justify=RIGHT)
entry.bind("<Return>", calculate)
entry.pack(pady=20, padx=20, fill="x")

label = Label(root, text="Calculator", font=("arial", 20, "bold"))
label.pack(pady=10)

buttonframe = Frame(root)
buttonframe.pack(pady=20)

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 1), ('.', 4, 0), ('+', 4, 3), ('=', 4, 2),
    ('C', 0, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        Button(buttonframe, text=text, font=("arial", 18), command=calculate, bg="lightblue").grid(row=row, column=col, sticky=W+E+N+S, padx=5, pady=5)
    elif text == 'C':
        Button(buttonframe, text=text, font=("arial", 18), command=lambda: entry.delete(0, END), bg="lightcoral").grid(row=row, column=col, sticky=W+E+N+S, padx=5, pady=5)
    else:
        Button(buttonframe, text=text, font=("arial", 18), command=lambda t=text: insert_text(t)).grid(row=row, column=col, sticky=W+E+N+S, padx=5, pady=5)

# Add some additional padding and configure rows
for i in range(5):
    buttonframe.rowconfigure(i, weight=1)

root.mainloop()
