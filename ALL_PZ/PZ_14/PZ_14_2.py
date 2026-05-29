# Задание 2 (вариант 15): GUI для задачи из ПЗ №9 — турагентства и туры в Италию и Канаду.

import tkinter as tk
from tkinter import ttk, scrolledtext

AGENCIES = {
    'Вояж': {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'},
    'РейнаТур': {'Англия', 'Япония', 'Канада', 'ЮАР'},
    'Радуга': {'США', 'Испания', 'Швеция', 'Австралия', 'Италия', 'Канада'},
}
TARGET = {'Италия', 'Канада'}


def find_agencies():
    result = [name for name, tours in AGENCIES.items() if TARGET.issubset(tours)]
    output.delete('1.0', tk.END)
    output.insert(tk.END, 'Туры в Италию и Канаду можно приобрести в:\n')
    if result:
        output.insert(tk.END, ', '.join(result))
    else:
        output.insert(tk.END, 'Подходящих агентств не найдено')


root = tk.Tk()
root.title('Туристические агентства')
root.geometry('480x320')

frame = ttk.Frame(root, padding=15)
frame.pack(fill='both', expand=True)

ttk.Label(frame, text='Поиск турагентств', font=('Segoe UI', 14, 'bold')).pack(anchor='w')
ttk.Label(
    frame,
    text='Определить, в каких агентствах можно купить туры в Италию и Канаду одновременно.',
).pack(anchor='w', pady=(5, 10))

ttk.Button(frame, text='Найти агентства', command=find_agencies).pack(anchor='w')

output = scrolledtext.ScrolledText(frame, width=50, height=10)
output.pack(fill='both', expand=True, pady=10)

root.mainloop()
