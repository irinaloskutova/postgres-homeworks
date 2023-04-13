"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2

"""Задаем переменные для списков, в которые будем складывать строки из csv файлов"""
customers = []
employees = []
orders = []

"""складываем в циклах строки в списки"""
with open('north_data/customers_data.csv', 'r') as f:
    data = csv.DictReader(f)
    for i in data:
        customers.append(i)

with open('north_data/employees_data.csv', 'r') as f:
    data = csv.DictReader(f)
    for i in data:
        employees.append(i)

with open('north_data/orders_data.csv', 'r') as f:
    data = csv.DictReader(f)
    for i in data:
        orders.append(i)

"""задаем переменные для соединения с базой данных"""
my_password = os.environ.get('PASSWORD_POSTGRESQL')
conn = psycopg2.connect(host="localhost", database="north", user="postgres", password=my_password)

"""заносим данные в базу данных"""
try:
    with conn:
        with conn.cursor() as cur:
            for i in range(len(customers)):
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (customers[i]['customer_id'],
                                                                          customers[i]['company_name'],
                                                                          customers[i]['contact_name']))
            for i in range(len(employees)):
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s)', (employees[i]['first_name'],
                                                                                  employees[i]['last_name'],
                                                                                  employees[i]['title'],
                                                                                  employees[i]['birth_date'],
                                                                                  employees[i]['notes']))
            for i in range(len(orders)):
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (orders[i]['order_id'],
                                                                               orders[i]['customer_id'],
                                                                               orders[i]['employee_id'],
                                                                               orders[i]['order_date'],
                                                                               orders[i]['ship_city']))
finally:
    conn.close()
