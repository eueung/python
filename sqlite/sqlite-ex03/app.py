import sqlite3
conn = sqlite3.connect('example.db')
# first, execute without c = conn.cursor()
#-------------------------------------
def execprint(strin):
	res = conn.execute(strin)
	for row in res:
	   print "ID = ", row[0]
	   print "NAME = ", row[1]
	   print "ADDRESS = ", row[2]
	   print "SALARY = ", row[3], "\n"
#-------------------------------------
conn.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY    NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);
''')
#-------------------------------------
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
execprint("SELECT id, name, address, salary  from COMPANY")
#-------------------------------------
conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
execprint("SELECT id, name, address, salary  from COMPANY where ID=1")
#-------------------------------------
conn.execute("DELETE from COMPANY where ID=2;")
for row in conn.execute("SELECT id, name, address, salary  from COMPANY;"):
	print row
#-------------------------------------
print "Total number of rows updated :", conn.total_changes
conn.commit()
conn.close()
#-------------------------------------