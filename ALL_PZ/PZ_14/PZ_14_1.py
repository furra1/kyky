# Задание 1: Реализовать прототип формы (Tkinter) по варианту 15.
import tkinter as tk
from tkinter import ttk, messagebox


def create_order():
    messagebox.showinfo("Заказ", "Заказ успешно создан!")


root = tk.Tk()
root.title("Создайте заказ")
root.geometry("730x730")
root.resizable(False, False)
root.configure(bg="#f4f4f4")  # Светло-серый фон как на скриншоте

# Настройка единого плоского стиля для полей ввода (ttk.Entry)
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Custom.TEntry",
    fieldbackground="white",
    bordercolor="#cccccc",
    lightcolor="#cccccc",
    darkcolor="#cccccc",
    padding=5
)

# Комбобоксы для времени
style.configure(
    "Custom.TCombobox",
    fieldbackground="white",
    bordercolor="#cccccc",
    lightcolor="#cccccc",
    darkcolor="#cccccc"
)

# --- Синяя шапка "Создайте заказ" ---
title_frame = tk.Frame(root, bg="#006d87", height=65)
title_frame.pack(fill="x")

title_label = tk.Label(
    title_frame,
    text="Создайте заказ",
    font=("Arial", 16),
    fg="white",
    bg="#006d87"
)
title_label.pack(pady=18)

# --- Главный контейнер формы ---
# Внутренний белый контур-рамка вокруг всей формы
border_frame = tk.Frame(root, bg="white", bd=1, relief="solid", highlightbackground="#cccccc")
border_frame.pack(fill="both", expand=True, padx=15, pady=15)

main_frame = tk.Frame(border_frame, bg="#f9f9f9", padx=25, pady=15)
main_frame.pack(fill="both", expand=True, padx=1, pady=1)

# Фиксированная ширина колонок: 0 - под кружки, 1 - под метки, 2 - под поля ввода
main_frame.columnconfigure(0, minsize=35)
main_frame.columnconfigure(1, minsize=180)
main_frame.columnconfigure(2, weight=1)


# Функция для создания красивых заголовков секций
def add_section_header(parent, number, text, row):
    # Голубой кружок с номером
    circle = tk.Label(
        parent,
        text=str(number),
        bg="#00a4d6",
        fg="white",
        font=("Arial", 11, "bold"),
        width=2,
        height=1
    )
    circle.grid(row=row, column=0, sticky="w", pady=(15, 10))

    # Текст заголовка секции
    label = tk.Label(
        parent,
        text=text,
        font=("Arial", 13, "bold"),
        bg="#f9f9f9",
        fg="#004c66"
    )
    label.grid(row=row, column=1, columnspan=2, sticky="w", padx=5, pady=(15, 10))


# --- СЕКЦИЯ 1: Информация о заказе ---
add_section_header(main_frame, 1, "Информация о заказе", row=0)

# Номер заказа *
lbl_order = tk.Label(main_frame, text="Номер заказа ", font=("Arial", 10), bg="#f9f9f9", fg="#333333")
lbl_order.grid(row=1, column=1, sticky="w", pady=6)
tk.Label(main_frame, text="*", font=("Arial", 10), bg="#f9f9f9", fg="red").place(in_=lbl_order, relx=1.0, x=-5)

order_entry = ttk.Entry(main_frame, width=54, style="Custom.TEntry")
order_entry.grid(row=1, column=2, sticky="w", pady=6)

# Название товара
tk.Label(main_frame, text="Название товара", font=("Arial", 10), bg="#f9f9f9", fg="#333333").grid(row=2, column=1, sticky="w", pady=6)
product_entry = ttk.Entry(main_frame, width=54, style="Custom.TEntry")
product_entry.grid(row=2, column=2, sticky="w", pady=6)

# Количество *
lbl_qty = tk.Label(main_frame, text="Количество ", font=("Arial", 10), bg="#f9f9f9", fg="#333333")
lbl_qty.grid(row=3, column=1, sticky="w", pady=6)
tk.Label(main_frame, text="*", font=("Arial", 10), bg="#f9f9f9", fg="red").place(in_=lbl_qty, relx=1.0, x=-5)

quantity_entry = ttk.Entry(main_frame, width=13, style="Custom.TEntry")
quantity_entry.grid(row=3, column=2, sticky="w", pady=6)


# --- СЕКЦИЯ 2: Контактная информация ---
add_section_header(main_frame, 2, "Контактная информация", row=4)

# Ваше имя
tk.Label(main_frame, text="Ваше имя", font=("Arial", 10), bg="#f9f9f9", fg="#333333").grid(row=5, column=1, sticky="w", pady=6)
name_entry = ttk.Entry(main_frame, width=54, style="Custom.TEntry")
name_entry.grid(row=5, column=2, sticky="w", pady=6)

# Ваш email *
lbl_email = tk.Label(main_frame, text="Ваш email ", font=("Arial", 10), bg="#f9f9f9", fg="#333333")
lbl_email.grid(row=6, column=1, sticky="w", pady=6)
tk.Label(main_frame, text="*", font=("Arial", 10), bg="#f9f9f9", fg="red").place(in_=lbl_email, relx=1.0, x=-5)

email_entry = ttk.Entry(main_frame, width=54, style="Custom.TEntry")
email_entry.grid(row=6, column=2, sticky="w", pady=6)

# Ваш телефон *
lbl_phone = tk.Label(main_frame, text="Ваш телефон ", font=("Arial", 10), bg="#f9f9f9", fg="#333333")
lbl_phone.grid(row=7, column=1, sticky="w", pady=6)
tk.Label(main_frame, text="*", font=("Arial", 10), bg="#f9f9f9", fg="red").place(in_=lbl_phone, relx=1.0, x=-5)

phone_entry = ttk.Entry(main_frame, width=27, style="Custom.TEntry")
phone_entry.insert(0, "+7 ( ")
phone_entry.grid(row=7, column=2, sticky="w", pady=4)

# Подпись формата под телефоном
phone_hint = tk.Label(main_frame, text="Формат: +7 (999) 999-99-99", font=("Arial", 9), bg="#f9f9f9", fg="#888888")
phone_hint.grid(row=8, column=2, sticky="w", pady=(0, 6))


# --- СЕКЦИЯ 3: Информация о доставке ---
add_section_header(main_frame, 3, "Информация о доставке", row=9)

# Адрес *
lbl_address = tk.Label(main_frame, text="Адрес ", font=("Arial", 10), bg="#f9f9f9", fg="#333333")
lbl_address.grid(row=10, column=1, sticky="nw", pady=6)
tk.Label(main_frame, text="*", font=("Arial", 10), bg="#f9f9f9", fg="red").place(in_=lbl_address, relx=1.0, x=-5)

# Многострочное текстовое поле с тонкой рамкой под адрес
address_text = tk.Text(main_frame, width=54, height=4, bd=1, relief="solid", highlightthickness=0, fg="#333333")
address_text.configure(bg="white", font=("Arial", 10))
address_text.grid(row=10, column=2, sticky="w", pady=6)

# Время доставки
tk.Label(main_frame, text="Время доставки", font=("Arial", 10), bg="#f9f9f9", fg="#333333").grid(row=11, column=1, sticky="w", pady=10)

time_frame = tk.Frame(main_frame, bg="#f9f9f9")
time_frame.grid(row=11, column=2, sticky="w", pady=10)

# Выпадающий список Часы
hours_cb = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(24)], width=4, state="readonly", style="Custom.TCombobox")
hours_cb.set("00")
hours_cb.pack(side="left")

tk.Label(time_frame, text=" : ", bg="#f9f9f9", font=("Arial", 10, "bold")).pack(side="left", padx=2)

# Выпадающий список Минуты
minutes_cb = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(0, 60, 5)], width=4, state="readonly", style="Custom.TCombobox")
minutes_cb.set("00")
minutes_cb.pack(side="left")

root.mainloop()
# Задание 1: Реализовать прототип формы (Tkinter) по варианту 15.
import tkinter as tk
from tkinter import ttk, messagebox


def create_order():
    messagebox.showinfo("Заказ", "Заказ успешно создан!")


root = tk.Tk()
root.title("Создайте заказ")
root.geometry("730x730")
root.resizable(False, False)
root.configure(bg="#f4f4f4")  # Светло-серый фон как на скриншоте

# Настройка единого плоского стиля для полей ввода (ttk.Entry)
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Custom.TEntry",
    fieldbackground="white",
    bordercolor="#cccccc",
    lightcolor="#cccccc",
    darkcolor="#cccccc",
    padding=5
)

# Комбобоксы для времени
style.configure(
    "Custom.TCombobox",
    fieldbackground="white",
    bordercolor="#cccccc",
    lightcolor="#cccccc",
    darkcolor="#cccccc"
)

# --- Синяя шапка "Создайте заказ" ---
title_frame = tk.Frame(root, bg="#006d87", height=65)
title_frame.pack(fill="x")

title_label = tk.Label(
    title_frame,
    text="Создайте заказ",
    font=("Arial", 16),
    fg="white",
    bg="#006d87"
)
title_label.pack(pady=18)

# --- Главный контейнер формы ---
# Внутренний белый контур-рамка вокруг всей формы
border_frame = tk.Frame(root, bg="white", bd=1, relief="solid", highlightbackground="#cccccc")
border_frame.pack(fill="both", expand=True, padx=15, pady=15)

main_frame = tk.Frame(border_frame, bg="#f9f9f9", padx=25, pady=15)
main_frame.pack(fill="both", expand=True, padx=1, pady=1)

# Фиксированная ширина колонок: 0 - под кружки, 1 - под метки, 2 - под поля ввода
main_frame.columnconfigure(0, minsize=35)
main_frame.columnconfigure(1, minsize=180)
main_frame.columnconfigure(2, weight=1)


# Функция для создания красивых заголовков секций
def add_section_header(parent, number, text, row):
    # Голубой кружок с номером
    circle = tk.Label(
        parent,
        text=str(number),
        bg="#00a4d6",
        fg="white",
        font=("Arial", 11, "bold"),
        width=2,
        height=1
    )
    circle.grid(row=row, column=0, sticky="w", pady=(15, 10))

    # Текст заголовка секции
    label = tk.Label(
        parent,
        text=text,
        font=("Arial", 13, "bold"),
        bg="#f9f9f9",
        fg="#004c66"
    )
    label.grid(row=row, column=1, columnspan=2, sticky="w", padx=5, pady=(15, 10))


# --- СЕКЦИЯ 1: Информация о заказе ---
add_section_header(main_frame, 1, "Информация о заказе", row=0)

# Номер заказа *
lbl_order = tk.Label(main_frame, text="Номер заказа ", font=("Arial", 10), bg="#f9f9f9", fg="#333333")
lbl_order.grid(row=1, column=1, sticky="w", pady=6)
tk.Label(main_frame, text="*", font=("Arial", 10), bg="#f9f9f9", fg="red").place(in_=lbl_order, relx=1.0, x=-5)

order_entry = ttk.Entry(main_frame, width=54, style="Custom.TEntry")
order_entry.grid(row=1, column=2, sticky="w", pady=6)

# Название товара
tk.Label(main_frame, text="Название товара", font=("Arial", 10), bg="#f9f9f9", fg="#333333").grid(row=2, column=1, sticky="w", pady=6)
product_entry = ttk.Entry(main_frame, width=54, style="Custom.TEntry")
product_entry.grid(row=2, column=2, sticky="w", pady=6)

# Количество *
lbl_qty = tk.Label(main_frame, text="Количество ", font=("Arial", 10), bg="#f9f9f9", fg="#333333")
lbl_qty.grid(row=3, column=1, sticky="w", pady=6)
tk.Label(main_frame, text="*", font=("Arial", 10), bg="#f9f9f9", fg="red").place(in_=lbl_qty, relx=1.0, x=-5)

quantity_entry = ttk.Entry(main_frame, width=13, style="Custom.TEntry")
quantity_entry.grid(row=3, column=2, sticky="w", pady=6)


# --- СЕКЦИЯ 2: Контактная информация ---
add_section_header(main_frame, 2, "Контактная информация", row=4)

# Ваше имя
tk.Label(main_frame, text="Ваше имя", font=("Arial", 10), bg="#f9f9f9", fg="#333333").grid(row=5, column=1, sticky="w", pady=6)
name_entry = ttk.Entry(main_frame, width=54, style="Custom.TEntry")
name_entry.grid(row=5, column=2, sticky="w", pady=6)

# Ваш email *
lbl_email = tk.Label(main_frame, text="Ваш email ", font=("Arial", 10), bg="#f9f9f9", fg="#333333")
lbl_email.grid(row=6, column=1, sticky="w", pady=6)
tk.Label(main_frame, text="*", font=("Arial", 10), bg="#f9f9f9", fg="red").place(in_=lbl_email, relx=1.0, x=-5)

email_entry = ttk.Entry(main_frame, width=54, style="Custom.TEntry")
email_entry.grid(row=6, column=2, sticky="w", pady=6)

# Ваш телефон *
lbl_phone = tk.Label(main_frame, text="Ваш телефон ", font=("Arial", 10), bg="#f9f9f9", fg="#333333")
lbl_phone.grid(row=7, column=1, sticky="w", pady=6)
tk.Label(main_frame, text="*", font=("Arial", 10), bg="#f9f9f9", fg="red").place(in_=lbl_phone, relx=1.0, x=-5)

phone_entry = ttk.Entry(main_frame, width=27, style="Custom.TEntry")
phone_entry.insert(0, "+7 ( ")
phone_entry.grid(row=7, column=2, sticky="w", pady=4)

# Подпись формата под телефоном
phone_hint = tk.Label(main_frame, text="Формат: +7 (999) 999-99-99", font=("Arial", 9), bg="#f9f9f9", fg="#888888")
phone_hint.grid(row=8, column=2, sticky="w", pady=(0, 6))


# --- СЕКЦИЯ 3: Информация о доставке ---
add_section_header(main_frame, 3, "Информация о доставке", row=9)

# Адрес *
lbl_address = tk.Label(main_frame, text="Адрес ", font=("Arial", 10), bg="#f9f9f9", fg="#333333")
lbl_address.grid(row=10, column=1, sticky="nw", pady=6)
tk.Label(main_frame, text="*", font=("Arial", 10), bg="#f9f9f9", fg="red").place(in_=lbl_address, relx=1.0, x=-5)

# Многострочное текстовое поле с тонкой рамкой под адрес
address_text = tk.Text(main_frame, width=54, height=4, bd=1, relief="solid", highlightthickness=0, fg="#333333")
address_text.configure(bg="white", font=("Arial", 10))
address_text.grid(row=10, column=2, sticky="w", pady=6)

# Время доставки
tk.Label(main_frame, text="Время доставки", font=("Arial", 10), bg="#f9f9f9", fg="#333333").grid(row=11, column=1, sticky="w", pady=10)

time_frame = tk.Frame(main_frame, bg="#f9f9f9")
time_frame.grid(row=11, column=2, sticky="w", pady=10)

# Выпадающий список Часы
hours_cb = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(24)], width=4, state="readonly", style="Custom.TCombobox")
hours_cb.set("00")
hours_cb.pack(side="left")

tk.Label(time_frame, text=" : ", bg="#f9f9f9", font=("Arial", 10, "bold")).pack(side="left", padx=2)

# Выпадающий список Минуты
minutes_cb = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(0, 60, 5)], width=4, state="readonly", style="Custom.TCombobox")
minutes_cb.set("00")
minutes_cb.pack(side="left")

root.mainloop()
