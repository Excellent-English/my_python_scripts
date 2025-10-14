import tkinter as tk
from tkinter.messagebox import showinfo

def hello():
    print("Witamy serdecznie przyjacielu!")

def clicked():
    showinfo(title="Info", message='Kliknięto')

root = tk.Tk()
root.title('Aplikacja testowa GUI')
root.geometry('600x400+350+180')
root.resizable(True,True)
root.minsize(300,300)
root.maxsize(600, 600)
# root.attributes('-alpha', 0.7)
# root.attributes('-topmost',1)
root.iconbitmap('flag.ico')


message1 = tk.Label(root, text="Witamy we Wrocławiu")
message1.pack()
message2 = tk.Label(root, text="Tekst nr 2")
message2.pack()
message3 = tk.Label(root, text="I kolejny tekst")
message3.pack()

button1 = tk.Button(root, text = "Hello", command=hello)
button1.pack(padx = 5, pady = 50)
button_exit = tk.Button(root, text = "Zamknij", command=root.quit)
button_exit.pack(ipadx = 50, ipady = 15, padx = 15, pady = 15)

icon = tk.PhotoImage(file='UKflag.png')
icon_small = icon.subsample(3,3)
button = tk.Button(text="Przycisk",image=icon_small, compound=tk.TOP, command=clicked)
button.pack()

root.mainloop()