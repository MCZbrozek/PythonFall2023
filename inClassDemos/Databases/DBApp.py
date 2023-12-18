import sqlite3


def get_all():
    conn = sqlite3.connect("demoDB.db")
    curs = conn.cursor()
    sql_cmd = 'SELECT ROWID, * FROM tblDemo'
    curs.execute(sql_cmd)
    data = curs.fetchall()
    conn.close()
    return data

def insert(row):
    conn = sqlite3.connect("demoDB.db")
    curs = conn.cursor()
    sql_cmd = 'INSERT INTO tblDemo (Num1Field, Num2Field, StringField) VALUES (?,?,?)'
    curs.execute(sql_cmd,row)
    conn.commit()
    conn.close()

def update(row_id, row):
    conn = sqlite3.connect("demoDB.db")
    curs = conn.cursor()
    sql_cmd = '''
        UPDATE tblDemo
        SET Num1Field = ?,
        Num2Field = ?, 
        StringField = ?
        WHERE ROWID = ?'''
    parameters = row + (row_id,)
    curs.execute(sql_cmd, parameters)
    conn.commit()
    conn.close()

def delete(row_id):
    conn = sqlite3.connect("demoDB.db")
    curs = conn.cursor()
    sql_cmd = '''
        DELETE FROM tblDemo
        WHERE ROWID = ?'''
    curs.execute(sql_cmd, (row_id,))
    conn.commit()
    conn.close()

def display_table(data):
    fmt = "%-3s %7s %7s %10s"
    print(fmt%('ID', 'Num1', 'Num2', 'Text'))
    for row in data:
        print(fmt%row)

def get_row_from_user():
    num1 = float(input("Please enter a floating point number: "))
    num2 = int(input("Please enter an integer: "))
    text = input("Please enter some text: ")
    return num1, num2, text # output will be a Tuple

def get_updated_row_from_user():
    row_id = int(input("Please enter row to update: "))
    row = get_row_from_user()
    return row_id,row

def get_delete_row_from_user():
    row_id = int(input("Please enter row to delete: "))
    return row_id


# start loop
while True:
    data = get_all()
    display_table(data)
    # print(data)

    option = input("(I)nsert, (U)pdate, (D)elete, (Q)uit: ")

    if option[0].lower() == 'q':
        break
    elif option[0].lower() == 'i':
        row = get_row_from_user()
        insert(row)
    elif option[0].lower() == 'u':
        row_id, row = get_updated_row_from_user()
        update(row_id, row)
    elif option[0].lower() == 'd':
        row_id = get_delete_row_from_user()
        delete(row_id)
print('Thank you for using this program')