import pandas as pd



excel_data = pd.read_excel("test.xlsx")

data = pd.DataFrame(excel_data)

dt = list(data)


list_morede_taeed = list(data['مبلغ مورد تایید'])
list_pardakht_shode = list(data['جمع هزينه هاي قابل پرداخت'])

for taeed, pardakht in zip(list_morede_taeed, list_pardakht_shode):
    if pardakht == 0:
        print("صفر در ردیف: ", list_pardakht_shode.index(pardakht))
    elif pardakht < int(taeed *0.9):
        print("ککم پرداخت شده در ردیف: ", list_pardakht_shode.index(pardakht))
        