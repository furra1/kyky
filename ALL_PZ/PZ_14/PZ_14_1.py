# Задание 1 (вариант 15): Реализовать прототип формы (Tkinter) по варианту 15.
# https://www.webasyst.ru/wa-data/public/updates/img/09/209/7355/7355.970.jpg

import tkinter as tk
from tkinter import ttk, messagebox


def on_save():
    messagebox.showinfo('Сохранение', 'Настройки сохранены')


def on_cancel():
    root.destroy()


root = tk.Tk()
root.title('Настройки приложения')
root.geometry('520x420')
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(fill='both', expand=True)

ttk.Label(frame, text='Настройки', font=('Segoe UI', 16, 'bold')).grid(row=0, column=0, columnspan=2, sticky='w', pady=(0, 15))

ttk.Label(frame, text='Название:').grid(row=1, column=0, sticky='w', pady=4)
name_entry = ttk.Entry(frame, width=40)
name_entry.insert(0, 'Моё приложение')
name_entry.grid(row=1, column=1, sticky='ew', pady=4)

ttk.Label(frame, text='Версия:').grid(row=2, column=0, sticky='w', pady=4)
version_entry = ttk.Entry(frame, width=40)
version_entry.insert(0, '1.0.0')
version_entry.grid(row=2, column=1, sticky='ew', pady=4)

ttk.Label(frame, text='Автор:').grid(row=3, column=0, sticky='w', pady=4)
author_entry = ttk.Entry(frame, width=40)
author_entry.insert(0, 'Matveychuk')
author_entry.grid(row=3, column=1, sticky='ew', pady=4)

ttk.Label(frame, text='Описание:').grid(row=4, column=0, sticky='nw', pady=4)
description = tk.Text(frame, width=30, height=5)
description.insert('1.0', 'Краткое описание приложения')
description.grid(row=4, column=1, sticky='ew', pady=4)

auto_update = tk.BooleanVar(value=True)
ttk.Checkbutton(frame, text='Автоматически проверять обновления', variable=auto_update).grid(
    row=5, column=0, columnspan=2, sticky='w', pady=10,
)

notify = tk.BooleanVar(value=False)
ttk.Checkbutton(frame, text='Уведомлять о новых версиях', variable=notify).grid(
    row=6, column=0, columnspan=2, sticky='w', pady=4,
)

btn_frame = ttk.Frame(frame)
btn_frame.grid(row=7, column=0, columnspan=2, pady=20)
ttk.Button(btn_frame, text='Сохранить', command=on_save).pack(side='left', padx=5)
ttk.Button(btn_frame, text='Отмена', command=on_cancel).pack(side='left', padx=5)

frame.columnconfigure(1, weight=1)
root.mainloop()
