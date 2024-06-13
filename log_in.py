from tkinter import *

def get_value():
    print("id: %s\npassword: %s" % (e1.get(), e2.get()))

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root = Tk()
root.title("Login Form")
root.geometry("400x200")

# Center the window
center_window(root)

frame = Frame(root, padx=20, pady=20)
frame.pack(expand=True)

Label(frame, text="ID", font=("Helvetica", 14, "bold")).grid(row=0, column=0, sticky=E, pady=5)
Label(frame, text="Password", font=("Helvetica", 14, "bold")).grid(row=1, column=0, sticky=E, pady=5)

e1 = Entry(frame)
e1.grid(row=0, column=1, pady=5, padx=10)

e2 = Entry(frame, show="*")
e2.grid(row=1, column=1, pady=5, padx=10)

button_frame = Frame(frame)
button_frame.grid(row=3, columnspan=2, pady=10)

Button(button_frame, text="OK", font=("Helvetica", 14, "bold"), command=get_value).pack(side=LEFT, padx=5)
Button(button_frame, text="Cancel", font=("Helvetica", 14, "bold"), command=root.quit).pack(side=LEFT, padx=5)

root.mainloop()
