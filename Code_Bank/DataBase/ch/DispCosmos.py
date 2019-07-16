import sqlite3
conn = sqlite3.connect("Cosmos.db", isolation_level=None)

c = conn.cursor()
c.execute("SELECT * FROM Member")

for row in c:
    print(row[0],row[1],row[2],row[3])

conn.close()
