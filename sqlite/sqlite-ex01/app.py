import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
#-------------------------------------
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#-------------------------------------
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print row
#-------------------------------------
conn.commit()
conn.close()
#-------------------------------------