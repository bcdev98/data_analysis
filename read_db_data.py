import sqlite3
from os import path

# current program file path
CurrPath = path.dirname(path.realpath(__file__))
print(CurrPath)

conn = sqlite3.connect(CurrPath + "/sample.db")
c = conn.cursor()
c.execute('SELECT email FROM users')
for row in c.fetchall():
    print(row[0])
