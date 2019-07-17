import sqlite3
conn = sqlite3.connect("shop.db", isolation_level=None)

# id name age section
sql = """
    CREATE TABLE Staff(
        name VARCHAR(20),
        age INTEGER,
        section VARCHAR(48)
    );
 """

conn.execute(sql)

conn.execute("INSERT INTO Staff VALUES('山野健太',25,'販売')")
conn.execute("INSERT INTO Staff VALUEs('川崎陽子',18,'販売')")
conn.execute("INSERT INTO Staff VALUEs('花尾翔',36,'仕入れ')")
conn.execute("INSERT INTO Staff VALUEs('大山海男',24,'経理')")
conn.execute("INSERT INTO Staff VALUEs('石井洋司',19,'販売')")

c = conn.cursor()
c.execute("SELECT * FROM Staff")
for row in c:
    print(row[0], row[1], row[2])

conn.close()
