# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

from tkinter import *

def read_file():
    lbl = Label(window)
    lbl.grid(column=1, row=1)
    with open(PATH_FILE, 'r', encoding='utf-8') as f:
        res = ""
        for line in f:
            res += line
            lbl.configure(text=res)

def write_file():
    with open(PATH_FILE, 'a', encoding='utf-8') as f:
        res = txt.get()
        f.writelines('\n'+ res)        

def find_file():
    
    lbl = Label(window)
    lbl.grid(column=2, row=2)
    with open(PATH_FILE, 'r', encoding='utf-8') as f:
        find_info = txt_find.get()
        for line in f:
            if find_info.casefold() in line.casefold():
                res = line
                lbl.configure(text=res)


def change_file():
    find_info = input()
    new_info = input()
    with open(PATH_FILE, 'r+', encoding='utf-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                lst = (line.strip()).split(' ')
                print(lst)




PATH_FILE = r'Telephonebook.txt'

window = Tk()
window.title("Добро пожаловать!")
window.geometry('1000x500')

# read_file(lbl)
txt = Entry(window, width=50)
txt.grid(column=0, row=1)
txt_find = Entry(window, width=50)
txt_find.grid(column=2, row=1)

btn_write = Button(window, text="добавить номер", command=write_file)
btn_write.grid(column=0, row=0)
btn_read = Button(window, text="показать список", command=read_file)
btn_read.grid(column=1, row=0)
btn_find = Button(window, text="найти номер", command=find_file)
btn_find.grid(column=2, row=0)


window.mainloop()



