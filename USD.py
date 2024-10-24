
from tkinter import *

import requests
from tkinter import messagebox as mb
from tkinter import ttk
def exchange():
    code=entry.get()

    if code:
        try:
            response=requests.get("https://open.er-api.com/v6/latest/USD")
            data=response.json()
            print(data)
            if code in data["rates"]:
                exchange_rates=data["rates"][code]
                mb.showerror("Курс обмена", f"Курс к долару{exchange_rates}{code}")



        except Exception as error:
            mb.showerror("Ошибка",f"ошибка{error}")

window=Tk()
window.geometry("600x500")
window.title("Конвертор валюты")
label=Label(text="Введите код валюты",font="Arial 15")
label.pack(pady=20)

popular_curs = ["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT",
"UZS"]
combobox=ttk.Combobox(value= popular_curs)
combobox.pack(pady=10)

entry=Entry()
entry.pack(pady=20)

b1=Button(text="Получить курс",command=exchange).pack(pady=10)



window.mainloop()