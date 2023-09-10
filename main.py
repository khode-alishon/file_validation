# Author = khode_alishon
# data validator for dental files
# 

from tkinter import *
import tkinter
import pandas as pd
from tkinter import ttk
import tkinterDnD as tkdnd # Importing the tkinterDnD module
import pyperclip

root = tkdnd.Tk()
root.title("سیستم ارزیابی خسارت ثبت شده")
x = root.winfo_screenwidth() // 2 -400 // 2
y = root.winfo_screenheight() // 2 - 400 // 2
root.geometry(f"400x400+{x}+{y}")
root.rowconfigure(0, weight = 2)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 2)
root.columnconfigure(0, weight=1)
root.config(bg = "#282c34")

def validate(*args):
    file_name = ""
    if args[1] == "dialoge":
        file_name = tkinter.filedialog.askopenfile(mode='r').name
        print(file_name)
    else:
        file_name = str(args[0].data).replace("{", "").replace("}", "")
    

    def valid(file):
                
        global number_of_errors
        number_of_errors = 1

        ###################################################

        validindow = Toplevel()
        validindow.config(bg = "black")
        validindow.columnconfigure(0, weigh = 1)
        x = root.winfo_screenwidth() // 2 -1482 // 2
        y = root.winfo_screenheight() // 2 - 600 // 2
        validindow.title(f"ارزیابی {file}")

        validindow.rowconfigure(0, weight = 1)
        validindow.geometry(f"1300x600+{x}+{y}")
        validindow.resizable(False,False)

        main_frame = Frame(validindow, bg="#343840")
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame, bg="#343840")
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(
            main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set, bg="#343840")
        my_canvas.bind("<Configure>", lambda e: my_canvas.configure(
            scrollregion=my_canvas.bbox("all")))

        top = Frame(my_canvas, bg="#343840")

        my_canvas.create_window((0, 0), window=top, anchor="nw")




        ##################################################

        row_label = Label(top,wraplength=300, text="ردیف", font="Btitr 18", bg="#343840", fg="#bbbcbd")
        row_label.grid(row=0, column=8, sticky=NSEW)

        personel_label = Label(top,wraplength=300,text="کد پرسنلی", font="Btitr 18",bg="#343840", fg="#bbbcbd")
        personel_label.grid(row=0, column=7, sticky=NSEW)

        name_label = Label(top,wraplength=300,text="نام بیمه شده", font="Btitr 18",bg="#343840", fg="#bbbcbd")
        name_label.grid(row=0, column=6, sticky=NSEW)

        ezhari_label = Label(top,wraplength=300,text="مبلغ اظهاری", font="Btitr 18",bg="#343840", fg="#bbbcbd")
        ezhari_label.grid(row=0, column=5, sticky=NSEW)

        taeedi_label = Label(top,wraplength=300,text="مبلغ تاییدی", font="Btitr 18",bg="#343840", fg="#bbbcbd")
        taeedi_label.grid(row=0, column=4, sticky=NSEW)

        pardakhty_label = Label(top,wraplength=300,text="مبلغ پرداختی", font="Btitr 18",bg="#343840", fg="#bbbcbd",)
        pardakhty_label.grid(row=0, column=3, sticky=NSEW)

        khesarat_label = Label(top,wraplength=300,text="نوع هزینه‌ی ریز بیماری", font="Btitr 18",bg="#343840", fg="#bbbcbd")
        khesarat_label.grid(row=0, column=2, sticky=NSEW)

        error_label = Label(top,wraplength=300,text="پیغام خطا", font="Btitr 18",bg="#343840", fg="#bbbcbd")
        error_label.grid(row=0, column=1, sticky=NSEW)

        sharh_label = Label(top,wraplength=300,text="شرح کسورات", font="Btitr 18",bg="#343840", fg="#bbbcbd")
        sharh_label.grid(row=0, column=0, sticky=NSEW)

        objects = []


        class Sefr():

            def copy(self, e, text):
                pyperclip.copy(text)


            def __init__(self, obj):
                global number_of_errors
                self.radif = obj[0]
                self.index = self.radif-1
                self.full_name = f"{obj[2]} {obj[3]}"
                
                self.personel = obj[1]
                self.ezhari = obj[7]
                self.taeedi = obj[8]
                self.pardakhty = obj[9]
                self.khesarat = obj[6]
                self.sharh = obj[39] if not pd.isna(obj[39]) else ""

                self.radif_label = Label(top,wraplength=300, text=f"{self.radif}", font="calibri 12 bold", bg = "#f24432", fg = "black")
                self.radif_label.grid(row=number_of_errors, column=8, sticky=NSEW)
                self.radif_label.bind("<Button-1>", lambda x: self.copy(x, text = self.radif_label["text"]))

                self.personel_label = Label(top,wraplength=300, text=f"{self.personel}", font="calibri 12 bold", bg = "#f24432", fg = "black")
                self.personel_label.grid(row=number_of_errors, column=7, sticky=NSEW)
                self.personel_label.bind("<Button-1>", lambda x: self.copy(x, text = self.personel_label["text"]))

                self.full_name_label = Label(top,wraplength=300, text=f"{self.full_name}", font="calibri 12 bold", bg = "#f24432", fg = "black")
                self.full_name_label.grid(row=number_of_errors, column=6, sticky=NSEW)
                self.full_name_label.bind("<Button-1>", lambda x: self.copy(x, text = self.full_name_label["text"]))

                self.ezhari_label = Label(top,wraplength=300, text=self.ezhari, font="calibri 12 bold", bg = "#f24432", fg = "black")
                self.ezhari_label.grid(row=number_of_errors, column=5, sticky=NSEW)
                self.ezhari_label.bind("<Button-1>", lambda x: self.copy(x, text = self.ezhari_label["text"]))

                self.taeedi_label = Label(top,wraplength=300, text=self.taeedi, font="calibri 12 bold", bg = "#f24432", fg = "black")
                self.taeedi_label.grid(row=number_of_errors, column=4, sticky=NSEW)
                self.taeedi_label.bind("<Button-1>", lambda x: self.copy(x, text = self.taeedi_label["text"]))

                self.pardakhty_label = Label(top,wraplength=300, text=self.pardakhty, font="calibri 12 bold", bg = "#f24432", fg = "black")
                self.pardakhty_label.grid(row=number_of_errors, column=3, sticky=NSEW)
                self.pardakhty_label.bind("<Button-1>", lambda x: self.copy(x, text = self.pardakhty_label["text"]))

                self.khesarat_label = Label(top,wraplength=300, text=self.khesarat, font="calibri 12 bold", bg = "#f24432", fg = "black")
                self.khesarat_label.grid(row=number_of_errors, column=2, sticky=NSEW)
                self.khesarat_label.bind("<Button-1>", lambda x: self.copy(x, text = self.khesarat_label["text"]))

                self.error_label = Label(top,wraplength=300, text="مبلغ قابل پرداخت خسات صفر می‌باشد", font="calibri 12 bold", bg = "#f24432", fg = "black")
                self.error_label.grid(row=number_of_errors, column=1, sticky=NSEW)
                self.error_label.bind("<Button-1>", lambda x: self.copy(x, text = "مبلغ قابل پرداخت خسات صفر می‌باشد"))

                self.sharh_label = Label(top,wraplength=300, text=self.sharh, font="calibri 12 bold", bg = "#f24432", fg = "black")
                self.sharh_label.grid(row=number_of_errors, column=0, sticky=NSEW)
                self.sharh_label.bind("<Button-1>", lambda x: self.copy(x, text = self.sharh_label["text"]))

                self.labels = [self.radif_label, self.personel_label, self.full_name_label, self.ezhari_label, self.taeedi_label,
                               self.pardakhty_label, self.khesarat_label, self.error_label, self.sharh_label]
                


                number_of_errors += 1


        class KamPardakhtShode():
            def copy(self, e, text):
                pyperclip.copy(text)


            def __init__(self, obj):
                global number_of_errors
                self.radif = obj[0]
                self.index = self.radif-1
                self.full_name = f"{obj[2]} {obj[3]}"
                
                self.personel = obj[1]
                self.ezhari = obj[7]
                self.taeedi = obj[8]
                self.pardakhty = obj[9]
                self.khesarat = obj[6]
                self.sharh = obj[39] if not pd.isna(obj[39]) else ""

                self.radif_label = Label(top,wraplength=300, text=f"{self.radif}", font="calibri 12 bold", bg = "#ffd712", fg = "black")
                self.radif_label.grid(row=number_of_errors, column=8, sticky=NSEW)
                self.radif_label.bind("<Button-1>", lambda x: self.copy(x, text = self.radif_label["text"]))

                self.personel_label = Label(top,wraplength=300, text=f"{self.personel}", font="calibri 12 bold", bg = "#ffd712", fg = "black")
                self.personel_label.grid(row=number_of_errors, column=7, sticky=NSEW)
                self.personel_label.bind("<Button-1>", lambda x: self.copy(x, text = self.personel_label["text"]))

                self.full_name_label = Label(top,wraplength=300, text=f"{self.full_name}", font="calibri 12 bold", bg = "#ffd712", fg = "black")
                self.full_name_label.grid(row=number_of_errors, column=6, sticky=NSEW)
                self.full_name_label.bind("<Button-1>", lambda x: self.copy(x, text = self.full_name_label["text"]))

                self.ezhari_label = Label(top,wraplength=300, text=self.ezhari, font="calibri 12 bold", bg = "#ffd712", fg = "black")
                self.ezhari_label.grid(row=number_of_errors, column=5, sticky=NSEW)
                self.ezhari_label.bind("<Button-1>", lambda x: self.copy(x, text = self.ezhari_label["text"]))

                self.taeedi_label = Label(top,wraplength=300, text=self.taeedi, font="calibri 12 bold", bg = "#ffd712", fg = "black")
                self.taeedi_label.grid(row=number_of_errors, column=4, sticky=NSEW)
                self.taeedi_label.bind("<Button-1>", lambda x: self.copy(x, text = self.taeedi_label["text"]))

                self.pardakhty_label = Label(top,wraplength=300, text=self.pardakhty, font="calibri 12 bold", bg = "#ffd712", fg = "black")
                self.pardakhty_label.grid(row=number_of_errors, column=3, sticky=NSEW)
                self.pardakhty_label.bind("<Button-1>", lambda x: self.copy(x, text = self.pardakhty_label["text"]))

                self.khesarat_label = Label(top,wraplength=300, text=self.khesarat, font="calibri 12 bold", bg = "#ffd712", fg = "black")
                self.khesarat_label.grid(row=number_of_errors, column=2, sticky=NSEW)
                self.khesarat_label.bind("<Button-1>", lambda x: self.copy(x, text = self.khesarat_label["text"]))

                self.error_label = Label(top,wraplength=300, text="کم پرداخت شده", font="calibri 12 bold", bg = "#ffd712", fg = "black")
                self.error_label.grid(row=number_of_errors, column=1, sticky=NSEW)
                self.error_label.bind("<Button-1>", lambda x: self.copy(x, text = "کم پرداخت شده"))

                self.sharh_label = Label(top,wraplength=300, text=self.sharh, font="calibri 12 bold", bg = "#ffd712", fg = "black")
                self.sharh_label.grid(row=number_of_errors, column=0, sticky=NSEW)
                self.sharh_label.bind("<Button-1>", lambda x: self.copy(x, text = self.sharh_label["text"]))

                self.labels = [self.radif_label, self.personel_label, self.full_name_label, self.ezhari_label, self.taeedi_label,
                               self.pardakhty_label, self.khesarat_label, self.error_label, self.sharh_label]
                


                number_of_errors += 1


        class KamTaeedShode():
            def copy(self, e, text):
                pyperclip.copy(text)

            def __init__(self, obj):
                global number_of_errors
                self.radif = obj[0]
                self.index = self.radif-1
                self.full_name = f"{obj[2]} {obj[3]}"
                
                self.personel = obj[1]
                self.ezhari = obj[7]
                self.taeedi = obj[8]
                self.pardakhty = obj[9]
                self.khesarat = obj[6]
                self.sharh = obj[39] if not pd.isna(obj[39]) else ""

                self.radif_label = Label(top,wraplength=300, text=f"{self.radif}", font="calibri 12 bold", bg = "#3ba9c2", fg = "black")
                self.radif_label.grid(row=number_of_errors, column=8, sticky=NSEW)
                self.radif_label.bind("<Button-1>", lambda x: self.copy(x, text = self.radif_label["text"]))

                self.personel_label = Label(top,wraplength=300, text=f"{self.personel}", font="calibri 12 bold", bg = "#3ba9c2", fg = "black")
                self.personel_label.grid(row=number_of_errors, column=7, sticky=NSEW)
                self.personel_label.bind("<Button-1>", lambda x: self.copy(x, text = self.personel_label["text"]))

                self.full_name_label = Label(top,wraplength=300, text=f"{self.full_name}", font="calibri 12 bold", bg = "#3ba9c2", fg = "black")
                self.full_name_label.grid(row=number_of_errors, column=6, sticky=NSEW)
                self.full_name_label.bind("<Button-1>", lambda x: self.copy(x, text = self.full_name_label["text"]))

                self.ezhari_label = Label(top,wraplength=300, text=self.ezhari, font="calibri 12 bold", bg = "#3ba9c2", fg = "black")
                self.ezhari_label.grid(row=number_of_errors, column=5, sticky=NSEW)
                self.ezhari_label.bind("<Button-1>", lambda x: self.copy(x, text = self.ezhari_label["text"]))

                self.taeedi_label = Label(top,wraplength=300, text=self.taeedi, font="calibri 12 bold", bg = "#3ba9c2", fg = "black")
                self.taeedi_label.grid(row=number_of_errors, column=4, sticky=NSEW)
                self.taeedi_label.bind("<Button-1>", lambda x: self.copy(x, text = self.taeedi_label["text"]))

                self.pardakhty_label = Label(top,wraplength=300, text=self.pardakhty, font="calibri 12 bold", bg = "#3ba9c2", fg = "black")
                self.pardakhty_label.grid(row=number_of_errors, column=3, sticky=NSEW)
                self.pardakhty_label.bind("<Button-1>", lambda x: self.copy(x, text = self.pardakhty_label["text"]))

                self.khesarat_label = Label(top,wraplength=300, text=self.khesarat, font="calibri 12 bold", bg = "#3ba9c2", fg = "black")
                self.khesarat_label.grid(row=number_of_errors, column=2, sticky=NSEW)
                self.khesarat_label.bind("<Button-1>", lambda x: self.copy(x, text = self.khesarat_label["text"]))

                self.error_label = Label(top,wraplength=300, text="کم تایید شده", font="calibri 12 bold", bg = "#3ba9c2", fg = "black")
                self.error_label.grid(row=number_of_errors, column=1, sticky=NSEW)
                self.error_label.bind("<Button-1>", lambda x: self.copy(x, text = "کم تایید شده"))

                self.sharh_label = Label(top,wraplength=300, text=self.sharh, font="calibri 12 bold", bg = "#3ba9c2", fg = "black")
                self.sharh_label.grid(row=number_of_errors, column=0, sticky=NSEW)
                self.sharh_label.bind("<Button-1>", lambda x: self.copy(x, text = self.sharh_label["text"]))

                self.labels = [self.radif_label, self.personel_label, self.full_name_label, self.ezhari_label, self.taeedi_label,
                               self.pardakhty_label, self.khesarat_label, self.error_label, self.sharh_label]
                
                


                number_of_errors += 1


                number_of_errors += 1


        excel_data = pd.read_excel(file)

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
            if eelami > taeedi and eelami *0.9 > taeedi:
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

        def resize(e):
            validindow.resizable(True, True)

        validindow.bind("<Return>", resize)


        validindow.mainloop()

    valid(file_name)



drop_label = ttk.Label(text = "کشیدن فایل", font="Btitr 18", ondrop = lambda e: validate(e, "drop"))
drop_label.config(background="#282c34", foreground="#ffffff")
drop_label.grid(row = 0 , column = 0)

or_Label = Label(text = "یا", font = "Btitr 16", bg = "#282c34", fg = "#ffffff")
or_Label.grid(row = 1, column = 0, sticky=NSEW)

open_Button = Button(root, text = "انتخاب فایل",font = "Btitr 18", command= lambda : validate("", "dialoge"), bg = "#282c34", fg ="#ffffff")
open_Button.grid(row = 2, column = 0, sticky=NSEW)

root.mainloop()
