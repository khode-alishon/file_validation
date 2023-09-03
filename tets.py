# how to print a whole row:
# for column in list(data.columns):
#   print(data[column][ROW_NUMBER])

import pandas as pd
from tkinter import *
from tkinter import ttk

global number_of_errors
number_of_errors = 1

###################################################

top = Tk()
top.config(bg = "black")
top.columnconfigure(0, weigh = 1)
top.columnconfigure(1, weigh = 1)
top.columnconfigure(2, weigh = 1)
top.rowconfigure(0, weight = 1)


##################################################

row_label = Label(top, text="ردیف", font="Btitr 18", bg="#343840", fg="#bbbcbd")
row_label.grid(row=0, column=2, sticky=NSEW)

name_label = Label(top,text="نام بیمه شده", font="Btitr 18",bg="#343840", fg="#bbbcbd")
name_label.grid(row=0, column=1, sticky=NSEW)

error_label = Label(top,text="پیغام خطا", font="Btitr 18",bg="#343840", fg="#bbbcbd")
error_label.grid(row=0, column=0, sticky=NSEW)

objects = []






# HERE.
# doing Sefr() and other classes for analyzing and showing data that's problematic


class Sefr():
    def __init__(self, obj):
        global number_of_errors
        self.radif = obj[0]
        self.index = self.radif-1
        self.full_name = f"{obj[2]} {obj[3]}"

        self.radif_label = Label(top,border=1, borderwidth=1, text=f"{self.radif}", font="calibri 12 bold", bg="#ff0000", fg="white")
        self.radif_label.grid(row=number_of_errors, column=2, sticky=NSEW)

        self.full_name_label = Label(top,border=1, borderwidth=1, text=f"{self.full_name}", font="calibri 12 bold", bg="#ff0000", fg="white")
        self.full_name_label.grid(row=number_of_errors, column=1, sticky=NSEW)

        self.error_label = Label(top,border=1, borderwidth=1, text="مبلغ قابل پرداخت خسات صفر می‌باشد", font="calibri 12 bold", bg="#ff0000", fg="white")
        self.error_label.grid(row=number_of_errors, column=0, sticky=NSEW)
        number_of_errors += 1


class KamPardakhtShode():
    def __init__(self, obj):
        global number_of_errors
        self.radif = obj[0]
        self.index = self.radif-1
        self.full_name = f"{obj[2]} {obj[3]}"

        self.radif_label = Label(top, text=f"{self.radif}", font="calibri 12 bold", bg="#ffd712", fg="white")
        self.radif_label.grid(row=number_of_errors, column=2, sticky=NSEW)

        self.full_name_label = Label(top, text=f"{self.full_name}", font="calibri 12 bold", bg="#ffd712", fg="white")
        self.full_name_label.grid(row=number_of_errors, column=1, sticky=NSEW)

        self.error_label = Label(top, text="کم پرداخت شده", font="calibri 12 bold", bg="#ffd712", fg="white")
        self.error_label.grid(row=number_of_errors, column=0, sticky=NSEW)
        number_of_errors += 1


class KamTaeedShode():
    def __init__(self, obj):
        global number_of_errors
        self.radif = obj[0]
        self.index = self.radif-1
        self.full_name = f"{obj[2]} {obj[3]}"

        self.radif_label = Label(top, text=f"{self.radif}", font="calibri 12 bold", bg="#3ba9c2", fg="white")
        self.radif_label.grid(row=number_of_errors, column=2, sticky=NSEW)

        self.full_name_label = Label(top, text=f"{self.full_name}", font="calibri 12 bold", bg="#3ba9c2", fg="white")
        self.full_name_label.grid(row=number_of_errors, column=1, sticky=NSEW)

        self.error_label = Label(top, text="کم تایید شده", font="calibri 12 bold", bg="#3ba9c2", fg="white")
        self.error_label.grid(row=number_of_errors, column=0, sticky=NSEW)
        number_of_errors += 1


excel_data = pd.read_excel("test.xlsx")

data = pd.DataFrame(excel_data)

dt = list(data)


list_eelami = list(data['مبلغ خسارت اعلام شده'])
list_morede_taeed = list(data['مبلغ مورد تایید'])
list_pardakht_shode = list(data['جمع هزينه هاي قابل پرداخت'])
list_radif = list(data['ردیف'])


def sefr_khorde(pardakhty):
    if pardakhty == 0:
        return True


def kam_pardakht_shode(taeedi, pardakhti):
   if pardakhti < int(taeedi * 0.9) and pardakhti != 0:
        return True
    

def kam_taeed_shode(eelami, taeedi):
    if eelami > taeedi:
        return True
    

for radif, eelami, taeedi, pardakhty in zip(list_radif, list_eelami, list_morede_taeed, list_pardakht_shode):

    if sefr_khorde(pardakhty):
        this = []
        for column in list(data.columns):
            this.append(list(data[column])[radif-1])
        Sefr(this)

    if kam_pardakht_shode(taeedi, pardakhty):
        this = []
        for column in list(data.columns):
            this.append(list(data[column])[radif-1])
        KamPardakhtShode(this)


    if kam_taeed_shode(eelami, taeedi):
        this = []
        for column in list(data.columns):
            this.append(list(data[column])[radif-1])
        KamTaeedShode(this)

for i in range(number_of_errors):
    top.rowconfigure(i, weight=1)

top.mainloop()
