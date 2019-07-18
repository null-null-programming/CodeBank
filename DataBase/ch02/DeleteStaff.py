import sqlite3
conn = sqlite3.connect("shop.db", isolation_level=None)

c = conn.cursor()
c.execute("SELECT * FROM Staff")

for row in c:
    print(row[0], row[1], row[2])

print(' ')

sql = "DELETE FROM Staff WHERE section='販売'"
conn.execute(sql)

c = conn.cursor()
c.execute("SELECT * FROM Staff")

for row in c:
    print(row[0], row[1], row[2])
