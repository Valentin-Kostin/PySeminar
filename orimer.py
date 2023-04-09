from tkinter import *
def clicked():
    with open(PATH_FILE, 'a', encoding='utf-8') as f:
        res = "Добро пожаловать, " + txt.get()
        # lbl.configure(text= res)
        f.writelines('\n'+ res)
    
PATH_FILE = r'Telephonebook.txt'
window = Tk()
window.title("Добро пожаловать!")
window.geometry('350x200')
lbl = Label(window, text="Привет!")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Нажми меня", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()