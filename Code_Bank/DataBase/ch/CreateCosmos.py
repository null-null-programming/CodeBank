import sqlite3
import os

conn = sqlite3.connect("Cosmos.db", isolation_level=None)

sql = """
    CREATE TABLE Member(
    id VARCHAR(4),
    name VARCHAR(20),
    age INTEGER,
    email VARCHAR(128)
    );
    """
conn.execute(sql)

sql = "INSERT INTO Member VALUES ('1018','Kenta',23,'ken@py.co.ja')"
conn.execute(sql)
sql = "INSERT INTO Member VALUES ('1027','Yamano',18,'yamachan@ab.cd')"
conn.execute(sql)
sql = "INSERT INTO Member VALUES ('1135','Honda',28,'honda@car.co.ja')"
conn.execute(sql)
sql = "INSERT INTO Member VALUES ('1333','Tomita',32,'tommy@py.co.ja')"
conn.execute(sql)

c = conn.cursor()
c.execute("SELECT * FROM Member")

for row in c:
    print(row)

conn.close()
