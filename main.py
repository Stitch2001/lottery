import random
import tkinter as tk
from tkinter import ttk
import time

with open('realFans.txt', 'r', encoding='utf-8') as f:
    fans = f.readlines()
    fans = [i.rstrip() for i in fans]


def onClickExecute():
    for fan in fans:
        text['text'] = fan
        text.update()
        time.sleep(0.1)
    s = len(fans)
    run = random.randint(0, s-1)
    fortunate = fans[run]
    text['text'] = fortunate
    text.update()


FONT = ('Times New Roman', 25)

mainForm = tk.Tk()
mainForm.title('地鼠大抽奖')

style = ttk.Style()
style.configure('my.TButton', font=('Times New Roman', 20))

text = ttk.Label(mainForm, text='会是你吗？', width=20, font=FONT)

text.pack(padx=5, pady=5)

execute = ttk.Button(mainForm, text='执行', width=25, style='my.TButton', command=onClickExecute)
execute.pack(padx=5, pady=5)

mainForm.mainloop()
