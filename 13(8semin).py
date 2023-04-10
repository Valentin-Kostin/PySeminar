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

def read_info():
    lbl = Label(window)
    lbl.grid(column=0, row=3)
    with open(PATH_FILE, 'r', encoding='utf-8') as f:
        res = ""
        for line in f:
            res += line
            lbl.configure(text=res)

def write_info():
    with open(PATH_FILE, 'a', encoding='utf-8') as f:
        res = txt.get()
        f.writelines('\n'+ res)        

def find_info():
    count = int(2)    
    with open(PATH_FILE, 'r', encoding='utf-8') as f:
        find_info = txt_find.get()
        
        for line in f:
            if find_info.casefold() in line.casefold():
                lbl = Label(window)
                lbl.grid(column=2, row=count)
                res = str(count - 1)+ ': ' + line
                lbl.configure(text=res)
                count += 1

def change_info():
    with open(PATH_FILE, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        find_info = txt_find.get()
        new_info = txt_new.get()
        for i in range(len(lines)):
            if find_info.casefold() in lines[i].casefold():
                lines[i] = new_info
                print(lines[i])
    with open(PATH_FILE, 'w+', encoding='utf-8') as f:
        f.writelines(lines)   

def delete_info():
    with open(PATH_FILE, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        find_info = txt_find.get()
        for i in range(len(lines)):
            if find_info.casefold() in lines[i].casefold():
                lines[i] = ''                
    with open(PATH_FILE, 'w+', encoding='utf-8') as f:
        f.writelines(lines)


PATH_FILE = r'Telephonebook.txt'

window = Tk()
window.title("Добро пожаловать!")
window.geometry('1000x400')

# read_info(lbl)
txt = Entry(window, width=40)
txt.grid(column=0, row=1)
txt_find = Entry(window, width=40)
txt_find.grid(column=2, row=1)
txt_new = Entry(window, width=40)
txt_new.grid(column=3, row=1)

btn_write = Button(window, text="добавить номер", command=write_info)
btn_write.grid(column=0, row=0)
btn_read = Button(window, text="показать список", command=read_info)
btn_read.grid(column=0, row=2)
btn_find = Button(window, text="найти номер", command=find_info)
btn_find.grid(column=2, row=0)
btn_change = Button(window, text="изменить найденый номер", command=change_info)
btn_change.grid(column=3, row=0)
btn_delete = Button(window, text="удалить найденый номер", command=delete_info)
btn_delete.grid(column=3, row=2)


window.mainloop()



