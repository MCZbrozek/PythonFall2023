import sqlite3
conn = sqlite3.connect('./demoDB.sqlite') 

curs = conn.cursor()

try:
    curs.execute('''
    CREATE TABLE tblDemo(
        Num1Field REAL,
        Num2Field INT,
        StringField TEXT
    )
    ''')


except sqlite3.OperationalError:
    print("Database already created with tblDemo")

starting_data = (
    (1.1,11,'Item 1'),
    (2.2,22,'Item 2'),
    (13.13,1313,'Item 13'),


)

for row in starting_data:
    sql_smd = '''
    INSERT INTO tblDemo (Num1Field, Num2Field, StringField)
    VALUES (?,?,?)
    '''
    curs.execute(sql_smd,row)

conn.commit() #execute our commands
conn.close() #close the database