# Author = khode_alishon
# data validator for dental files
# 
# *** check test.py ***


from tkinter import *
import tkinter
from tkinter import ttk
import tkinterDnD as tkdnd # Importing the tkinterDnD module

root = tkdnd.Tk()
root.geometry("400x400")
root.rowconfigure(0, weight = 2)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 2)
root.columnconfigure(0, weight=1)

def validate(*args):
    file_name = ""
    if args[1] == "dialoge":
        file_name = tkinter.filedialog.askopenfile(mode='r').name
        print(file_name)
    else:
        file_name = str(args[0].data).replace("{", "").replace("}", "")
    
    with open(file_name, "r") as file:
        a = file.readlines()
        print(a)

drop_label = ttk.Label(text = "کشیدن فایل", font="Btitr 18", ondrop = lambda e: validate(e, "drop"))
drop_label.grid(row = 0 , column = 0)

or_Label = Label(text = "یا", font = "Btitr 12")
or_Label.grid(row = 1, column = 0, sticky=NSEW)

open_Button = Button(root, text = "انتخاب فایل",font = "Btitr 18", command= lambda : validate("", "dialoge"))
open_Button.grid(row = 2, column = 0, sticky=NSEW)



root.mainloop()