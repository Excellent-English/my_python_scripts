import tkinter as tk
from tkinter.messagebox import showinfo

from PyInstaller.loader.pyiboot01_bootstrap import entry

root = tk.Tk()
entry_text = tk.StringVar()

frame = tk.Frame()
frame.pack(padx=50, pady=50)
label = tk.Label(frame, text = "Wpisz imię")
label.pack()

entry = tk.Entry(frame, font=('Helvetica', 20), textvariable=entry_text)
entry.pack()

text_field = tk.Text(frame, height = 3, width = 30)
text_field.pack()

button_entry = tk.Button(frame, text='Złap imię', command=imie)
button_entry.pack(ipadx=5,ipady=5,fill='x')
button_text = tk.Button(frame, text='Złap komentarz', command=opinia)
button_text.pack(ipadx=5,ipady=5)

root.mainloop()