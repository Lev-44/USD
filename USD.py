
from tkinter import *

import requests
from tkinter import messagebox as mb
from tkinter import ttk

def update_cur(event):
    code=combobox.get()

    name_rus=curses[code]
    cur_label.config(text=name_rus)

def exchange():
    code=combobox.get()


    if code:
        try:
            #name_rus =cur[code]
            response=requests.get("https://open.er-api.com/v6/latest/USD")
            data=response.json()
            print(data)
            if code in data["rates"]:
                exchange_rates=data["rates"][code]
                mb.showinfo("Курс обмена", f"Курс к долару{exchange_rates:.1f}{code}")



        except Exception as error:
            mb.showerror("Ошибка",f"ошибка{error}")

window=Tk()
window.geometry("600x500")
window.title("Конвертор валюты")
label=Label(text="Введите код валюты",font="Arial 15")
label.pack(pady=20)

curses = {
"EUR": "Евро",
"JPY": "Японская йена",
"GBP": "Британский фунт стерлингов",
"AUD": "Австралийский доллар",
"CAD": "Канадский доллар",
"CHF": "Швейцарский франк",
"CNY": "Китайский юань",
"RUB": "Российский рубль",
"KZT": "Казахстанский тенге",
"UZS": "Узбекский сум"
}

popular_curs = ["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT",
"UZS"]
combobox=ttk.Combobox(value= list(curses.keys()))
combobox.bind("<<ComboboxSelected>>", update_cur)
combobox.pack(pady=10)

cur_label=ttk.Label()
cur_label.pack(pady=10,padx=10)

#entry=Entry()
#entry.pack(pady=20)

b1=Button(text="Получить курс",command=exchange).pack(pady=10)



window.mainloop()