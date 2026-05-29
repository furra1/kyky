# Задание (вариант 15): Приложение «РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ».
# Таблица Расходы: Дата, Код продукта, Наименование продукта, Расходы, Сумма.

import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'rashody.db')

SAMPLE_DATA = [
    ('2025-01-10', 'P001', 'Молоко сгущённое', 'Сырьё', 12500.50),
    ('2025-01-11', 'P002', 'Печенье «Юбилейное»', 'Упаковка', 3200.00),
    ('2025-01-12', 'P001', 'Молоко сгущённое', 'Электроэнергия', 890.75),
    ('2025-01-13', 'P003', 'Конфеты «Алёнка»', 'Сырьё', 15600.00),
    ('2025-01-14', 'P002', 'Печенье «Юбилейное»', 'Зарплата', 45000.00),
    ('2025-01-15', 'P004', 'Хлеб белый', 'Сырьё', 5400.20),
    ('2025-01-16', 'P003', 'Конфеты «Алёнка»', 'Упаковка', 2100.00),
    ('2025-01-17', 'P005', 'Сок яблочный', 'Сырьё', 9800.00),
    ('2025-01-18', 'P004', 'Хлеб белый', 'Амортизация', 1500.00),
    ('2025-01-19', 'P005', 'Сок яблочный', 'Транспорт', 2300.50),
]


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS rashody (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                kod_produkta TEXT NOT NULL,
                naimenovanie TEXT NOT NULL,
                vid_rashodov TEXT NOT NULL,
                summa REAL NOT NULL
            )
        ''')
        count = conn.execute('SELECT COUNT(*) FROM rashody').fetchone()[0]
        if count == 0:
            conn.executemany(
                'INSERT INTO rashody (data, kod_produkta, naimenovanie, vid_rashodov, summa) '
                'VALUES (?, ?, ?, ?, ?)',
                SAMPLE_DATA,
            )
            print('Добавлено 10 начальных записей.')
        conn.commit()


def print_rows(rows):
    if not rows:
        print('Записи не найдены.')
        return
    for row in rows:
        print(
            f"ID={row[0]} | {row[1]} | код={row[2]} | {row[3]} | "
            f"расход={row[4]} | сумма={row[5]:.2f}"
        )


def show_all():
    with get_connection() as conn:
        rows = conn.execute(
            'SELECT id, data, kod_produkta, naimenovanie, vid_rashodov, summa '
            'FROM rashody ORDER BY id'
        ).fetchall()
    print('\nВсе записи:')
    print_rows(rows)


def add_record():
    try:
        data = input('Дата (ГГГГ-ММ-ДД): ').strip()
        kod = input('Код продукта: ').strip()
        name = input('Наименование продукта: ').strip()
        vid = input('Вид расходов: ').strip()
        summa = float(input('Сумма: ').replace(',', '.'))
    except ValueError:
        print('Ошибка: неверный формат суммы.')
        return
    with get_connection() as conn:
        conn.execute(
            'INSERT INTO rashody (data, kod_produkta, naimenovanie, vid_rashodov, summa) '
            'VALUES (?, ?, ?, ?, ?)',
            (data, kod, name, vid, summa),
        )
        conn.commit()
    print('Запись добавлена.')


def search_menu():
    print('\n--- Поиск (3 SQL-запроса) ---')
    print('1 — по коду продукта')
    print('2 — по дате')
    print('3 — по наименованию (LIKE)')
    choice = input('Выбор: ').strip()
    with get_connection() as conn:
        if choice == '1':
            kod = input('Код продукта: ').strip()
            rows = conn.execute(
                'SELECT id, data, kod_produkta, naimenovanie, vid_rashodov, summa '
                'FROM rashody WHERE kod_produkta = ?',
                (kod,),
            ).fetchall()
        elif choice == '2':
            data = input('Дата: ').strip()
            rows = conn.execute(
                'SELECT id, data, kod_produkta, naimenovanie, vid_rashodov, summa '
                'FROM rashody WHERE data = ?',
                (data,),
            ).fetchall()
        elif choice == '3':
            part = input('Фрагмент наименования: ').strip()
            rows = conn.execute(
                'SELECT id, data, kod_produkta, naimenovanie, vid_rashodov, summa '
                'FROM rashody WHERE naimenovanie LIKE ?',
                (f'%{part}%',),
            ).fetchall()
        else:
            print('Неверный выбор.')
            return
    print_rows(rows)


def delete_menu():
    print('\n--- Удаление (3 SQL-запроса) ---')
    print('1 — по ID')
    print('2 — по коду продукта')
    print('3 — по виду расходов')
    choice = input('Выбор: ').strip()
    with get_connection() as conn:
        if choice == '1':
            record_id = int(input('ID: '))
            cur = conn.execute('DELETE FROM rashody WHERE id = ?', (record_id,))
        elif choice == '2':
            kod = input('Код продукта: ').strip()
            cur = conn.execute('DELETE FROM rashody WHERE kod_produkta = ?', (kod,))
        elif choice == '3':
            vid = input('Вид расходов: ').strip()
            cur = conn.execute('DELETE FROM rashody WHERE vid_rashodov = ?', (vid,))
        else:
            print('Неверный выбор.')
            return
        conn.commit()
        print(f'Удалено записей: {cur.rowcount}')


def update_menu():
    print('\n--- Редактирование (3 SQL-запроса) ---')
    print('1 — изменить сумму по ID')
    print('2 — изменить наименование по ID')
    print('3 — изменить вид расходов по ID')
    choice = input('Выбор: ').strip()
    try:
        record_id = int(input('ID записи: '))
    except ValueError:
        print('Ошибка: ID должен быть числом.')
        return
    with get_connection() as conn:
        if choice == '1':
            summa = float(input('Новая сумма: ').replace(',', '.'))
            cur = conn.execute(
                'UPDATE rashody SET summa = ? WHERE id = ?',
                (summa, record_id),
            )
        elif choice == '2':
            name = input('Новое наименование: ').strip()
            cur = conn.execute(
                'UPDATE rashody SET naimenovanie = ? WHERE id = ?',
                (name, record_id),
            )
        elif choice == '3':
            vid = input('Новый вид расходов: ').strip()
            cur = conn.execute(
                'UPDATE rashody SET vid_rashodov = ? WHERE id = ?',
                (vid, record_id),
            )
        else:
            print('Неверный выбор.')
            return
        conn.commit()
        print(f'Обновлено записей: {cur.rowcount}')


def main():
    init_db()
    actions = {
        '1': show_all,
        '2': add_record,
        '3': search_menu,
        '4': delete_menu,
        '5': update_menu,
    }
    while True:
        print('\n=== РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ ===')
        print('1 — показать все записи')
        print('2 — добавить запись')
        print('3 — поиск')
        print('4 — удаление')
        print('5 — редактирование')
        print('0 — выход')
        cmd = input('Команда: ').strip()
        if cmd == '0':
            break
        action = actions.get(cmd)
        if action:
            try:
                action()
            except sqlite3.Error as e:
                print(f'Ошибка БД: {e}')
            except ValueError as e:
                print(f'Ошибка ввода: {e}')
        else:
            print('Неизвестная команда.')


if __name__ == '__main__':
    main()
