import psycopg2
import csv
import re
from config import config

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


while True:
    params = config()
    conn = psycopg2.connect(**params)
    sql = 'select * from PhoneBook '
    cursor = conn.cursor()
    cursor.execute(sql)
    PhoneBook = cursor.fetchall()
    n = input()
    if n == 'sorted data':
        a = PhoneBook
        a.sort(key=lambda tup: tup[0], reverse=False)
        for i in a:
            for j in i:
                print(j, end=' ')
            print()
    if n == 'reversed sorted data':
        a = PhoneBook
        a.sort(key=lambda tup: tup[0], reverse=True)
        for i in a:
            for j in i:
                print(j, end=' ')
            print()
    if str(n) == 'data':

        for i in PhoneBook:
            for j in i:
                print(j, end=' ')
            print()

    elif str(n) == 'insert':
        nn = input().split(" ")
        a = len(nn)
        i = 0
        while i < a:

            sql = f'select * from PhoneBook where name = \'{nn[i]}\''
            cursor = conn.cursor()
            cursor.execute(sql)
            res = cursor.fetchall()
            print(res)
            cursor.execute(f"DELETE FROM PhoneBook WHERE name='{nn[i]}'")
            print(nn[i])
            if is_int(nn[i + 1]):

                if not res:

                    cursor.execute("INSERT INTO PhoneBook (name,phone) VALUES (%s, %s)", (nn[i], nn[i + 1]))
                    # print(nn)
                    print("New user is added")
                    conn.commit()
                else:
                    cursor.execute(f"DELETE FROM PhoneBook WHERE name='{nn[i]}'")
                    cursor.execute("INSERT INTO PhoneBook (name,phone) VALUES (%s, %s)", (nn[i], nn[i + 1]))
                    conn.commit()
                    print("User is updated")
                #print(MyContacts)
                i += 2

            else:
                print("Phone Error")
                i += 2
    elif str(n) == 'delete':
        nn = input().split(" ")
        for i in nn:
            cursor.execute(f"DELETE FROM PhoneBook WHERE name='{i}'")
            print("User is deleted")

        conn.commit()
    elif str(n) == "update":
        nn = input()
        if is_int(nn):
            m = input()
            #print(nn)
            cursor.execute(f"DELETE FROM PhoneBook WHERE name='{m}'")
            cursor.execute(f"DELETE FROM PhoneBook WHERE phone='{nn}'")
            cursor.execute("INSERT INTO PhoneBook (name,phone) VALUES (%s, %s)", (m, nn))
            conn.commit()
        else:
            m = input()
            cursor.execute(f"DELETE FROM PhoneBook WHERE name='{nn}'")
            cursor.execute(f"DELETE FROM PhoneBook WHERE phone='{m}'")
            cursor.execute("INSERT INTO PhoneBook (name,phone) VALUES (%s, %s)", (nn, m))
            conn.commit()
    elif str(n) == 'find person':
        mm = str(input())
        b = []

        for i in PhoneBook:
            if mm.lower() in i[0].lower():
                b.append(i)
                print(b)
