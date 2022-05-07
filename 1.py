#!/usr/bin/python

import psycopg2
from config import config
import csv
import re


def create_tables():
    command = """
        CREATE TABLE PhoneBook (
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL
        )
        """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except:
        return 0
    finally:
        if conn is not None:
            conn.close()


def insert_user(name, phone):
    global cur
    command = """INSERT INTO phonebook(name, phone)
    VALUES (%s, %s);"""
    cur.execute(command, (name, phone))

def insert_user_csv(file):
    global cur
    command = """INSERT INTO phonebook(name, phone)
        VALUES (%s, %s);"""
    with open(file, 'r') as f:
        reader = f.read()
        r = re.split('\n', reader)
        for row in r[:len(r) - 1]:
            a = re.split(';', row)
            cur.execute(command, (a[0], a[1]))


def update_name(name, smt):
    global cur
    if '+' in smt:
        a = 'phone'
    else:
        a = 'name'
    command = f"""UPDATE public.phonebook
    SET name = %s
    WHERE {a} = %s"""
    cur.execute(command, (name, smt))


def update_phone(phone, smt):
    global cur
    if '+' in smt:
        a = 'phone'
    else:
        a = 'name'
    command = f"""UPDATE public.phonebook
    SET phone = %s
    WHERE {a} = %s"""
    cur.execute(command, (phone, smt))


def delete_user(name):
    global cur
    command = """DELETE FROM public.phonebook
    WHERE name = %s"""
    cur.execute(command, (name,))


def show():
    global cur, a
    nnn = ["name", "phone", "name, phone"]
    cur.execute(f"SELECT {nnn[a - 1]} FROM public.phonebook;")
    return cur.fetchall()


if __name__ == '__main__':
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        create_tables()
        what = int(input('What do you want?\n'
                         '1.insert   |   2.update   |   3.delete   |   4.show\n'))
        if what == 1:
            a = int(input('1.загрузить данные из csv файла\n'
                          '2.ввод имени пользователя, телефона из консоли\n'))
            if a == 2:
                name = input('Enter the name\n')
                phone = input('Enter the phone number\n')
                insert_user(name, phone)
            if a == 1:
                b = input('Введите путь к файлу')
                insert_user_csv(b)
        if what == 2:
            p_or_n = int(input('Do you want to change name or phone number?\n'
                               '1.name   |   2.phone\n'))
            if p_or_n == 1:
                phone_or_curname = input('Введите номер телефона или текущее имя\n')
                new_name = input('Введите новое имя\n')
                update_name(new_name, phone_or_curname)
            if p_or_n == 2:
                phone_or_curname = input('Введите номер телефона или текущее имя\n')
                new_phone = input('Введите новый номер телефона\n')
                update_phone(new_phone, phone_or_curname)
        if what == 3:
            name = input('Введите имя контакта\n')
            delete_user(name)
        if what == 4:
            a = int(input('Вывести\n'
                          '1.только имена   |   2.только номера    |    3.имя и номер\n'))
            [print(i, j, end='\n') for i, j in show()]
        conn.commit()
        cur.close()
    finally:
        if conn is not None:
            conn.close()
