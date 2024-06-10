from tkinter import *
from googletrans import Translator, LANGUAGES

# Initialize the Translator
tarjimon = Translator()

def translate_text():
    text = entry.get()
    if text.lower() == 'stop':
        root.quit()
    else:
        try:
            translated = tarjimon.translate(text, src='en', dest='ko')
            result_label.config(text=f"{translated.origin} --> {translated.text}")
        except Exception as e:
            result_label.config(text="Translation error. Please try again.")

root = Tk()
root.geometry("500x400")
root.title("English to Korean Translator")

# Main frame
main_frame = Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill=BOTH)

# Entry label
entry_label = Label(main_frame, text="Enter text to translate:", font=("arial", 14))
entry_label.pack(pady=10)

# Entry widget
entry = Entry(main_frame, font=("arial", 18), width=30, borderwidth=2, relief="solid")
entry.pack(pady=10)

# Button to trigger translation
translate_button = Button(main_frame, text="Translate", font=("arial", 14), command=translate_text, bg="lightblue", fg="white", activebackground="blue", activeforeground="white", padx=10, pady=5)
translate_button.pack(pady=10)

# Label to display result
result_label = Label(main_frame, text="Translation will appear here.", font=("arial", 14), wraplength=400, justify=LEFT, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
result_label.pack(pady=20, fill=X)

root.mainloop()
