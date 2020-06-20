# Задание 3
# Работаем с таблицей в БД из кода.
# Написать cli-программу, которая бы имитировала дневник трат:
# 1) Схема таблицы представлена в dbml нотации. Необходимо при старте программы создать таблицу
# которая бы ей полностью соответствовала, если такая таблица не существует.
# 2) Предусмотрена функция чтения по датам: пользователь введя дату получает cписок того что он покупал в этот день
# и общую сумму трат в день. Если записей на указанную дату нет — вывести об этом сообщение.
# 3) Предусмотрено добавление новой записи в таблицу: с клавиатуры вводится дата,
# наименование покупки и потраченная сумма денег
# 4) Предусмотрено удаление записи по id.
# 5) Можно отменить операцию вместо ввода данных.
# 6) В случае некорректного ввода вывести на экран на человеко-читаемом русском языке сообщение
# о некорректности ввода и запросить у пользователя повторный ввод данных или отмену операции.

# Table Expenses as E {
#   id bigint [pk, not null, unique, increment, note: 'Уникальный идентификатор траты']
#   date date [not null, note: 'Дата, в которую была произведена покупка']
#   name varchar(25) [not null, note:'Наименование траты']
#   money double [not null, note: 'Количество потраченных денег, руб.']
# }

import sqlite3
conn = sqlite3.connect('excersize4.db')
c = conn.cursor()


def create_table():
    """Создаёт бд"""
    c.execute("CREATE TABLE IF NOT EXISTS Expenses("
              "id AUTO_INCREMENT INTEGER NOT NULL PRIMARY KEY,"
              "date DATE NOT NULL,"
              "name VARCHAR(25) NOT NULL,"
              "money REAL NOT NULL)")


create_table()


def input_func():
    date = input("Date: ")
    summ = input("Summa: ")
    name = input("Name: ")
    c.execute("INSERT INTO Expenses(date, name, money) VALUES (?, ?, ?)", (date, name, summ))
    conn.commit()


input_func()


