# Задание 2: GUI для задачи из ПЗ №7.
# 1. Подсчитать строчные латинские и русские буквы.
# 2. Подсчитать знаки препинания в предложении.

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

PUNCTUATION = '.,;:-?!()[]{}<>"\'/'


def count_lowercase_letters(text):
    return sum(1 for char in text if char.islower())


def count_punctuation(text):
    return sum(1 for char in text if char in PUNCTUATION)


def analyze():
    text = text_input.get('1.0', tk.END).strip()
    if not text:
        messagebox.showwarning('Внимание', 'Введите текст для анализа.')
        return
    lower_count = count_lowercase_letters(text)
    punct_count = count_punctuation(text)
    result.delete('1.0', tk.END)
    result.insert(
        tk.END,
        f'Строчных букв (латиница и кириллица): {lower_count}\n'
        f'Знаков препинания: {punct_count}\n',
    )


root = tk.Tk()
root.title('ПЗ №7 — анализ строки')
root.geometry('520x400')

frame = ttk.Frame(root, padding=15)
frame.pack(fill='both', expand=True)

ttk.Label(frame, text='Анализ строки (ПЗ №7)', font=('Segoe UI', 14, 'bold')).pack(anchor='w')
ttk.Label(frame, text='Введите строку или предложение:').pack(anchor='w', pady=(8, 4))

text_input = scrolledtext.ScrolledText(frame, width=55, height=8)
text_input.pack(fill='both', expand=True)
text_input.insert('1.0', 'Привет, world! Это тест: 123.')

ttk.Button(frame, text='Подсчитать', command=analyze).pack(anchor='w', pady=8)

result = scrolledtext.ScrolledText(frame, width=55, height=5, state='normal')
result.pack(fill='both', expand=True)

root.mainloop()
