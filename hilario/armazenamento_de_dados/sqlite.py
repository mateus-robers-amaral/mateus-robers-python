import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
cursor.execute('''
create table''')