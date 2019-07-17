import sqlite3
conn = sqlite3.connect("Sample.db", isolation_level=None)

# data code quantitiy
# dataは2020/12/15などという形式
sql = """
CREATE TABLE Sales(
    data VARCHAR(10),
    code VARCHAR(5),
    quantity INTEGER
);
"""

conn.execute(sql)

conn.execute("INSERT INTO Sales VALUES('2020/12/15','20023',15)")
conn.execute("INSERT INTO Sales VALUES('2020/11/15','42102',28)")
conn.execute("INSERT INTO Sales VALUES('2020/02/15','52300',14)")
conn.execute("INSERT INTO Sales VALUES('2019/10/03','31010',21)")

c = conn.cursor()
c.execute("SELECT * FROM Sales")
for row in c:
    print(row[0], row[1], row[2])

conn.close()
