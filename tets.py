# how to print a whole row:
# for column in list(data.columns):
#   print(data[column][ROW_NUMBER])

import pandas as pd
from tkinter import *

root = Tk()

objects = []

### HERE.
### doing Sefr() and other classes for analyzing and showing data that's problematic

class Sefr():
    def __init__(self, obj):
        self.radif = obj[0]
        self.index = self.radif-1
        self.full_name = f"{obj[2]} {obj[3]}"
        print(self.radif, self.index, self.full_name)



class KamPardakhtShode():
    def __init__(self, obj):
        pass


class KamTaeedShode():
    def __init__(self, obj):
        pass

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
    if pardakhti < int(taeedi * 0.9):
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
        objects.append(KamPardakhtShode(radif))
        
    if kam_taeed_shode(eelami, taeedi):
        objects.append(KamTaeedShode(radif))
        






root.mainloop()