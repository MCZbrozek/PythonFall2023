import sqlite3
import InventoryItem as InventoryItem

def init_db():
    conn = sqlite3.connect('inventoryDB.db')
    curs = conn.cursor()

    try:
        curs.execute('''
    CREATE TABLE tblInventoryItem (
            serial_number INT,
            description TEXT,
            location TEXT,
            date_arrived TEXT,
            date_left TEXT
            )              
    ''')
    except sqlite3.OperationalError:
        print('Database already created.')

        conn.commit()
        conn.close()

def get_all():
    conn = sqlite3.connect('inventoryDB.db')
    curs = conn.cursor()
    cmd = '''SELECT ROWID, * FROM tblInventoryItem;'''
    curs.execute(cmd)
    rows = curs.fetchall()
    conn.commit()
    conn.close

    items = []
    for row in rows:
        item = InventoryItem
        item.row_id = row[0]
        item.serial_number = row[1]
        item.description = row[2]
        item.location = row[3]
        item.date_arrived = row[4]
        item.date_left = row[5]
        items.append(item)
     # returns a list of tuples
    return items

def get_by_id():
    conn = sqlite3.connect('inventoryDB.db')
    curs = conn.cursor()
    cmd = '''SELECT ROWID, * FROM tblInventoryItem; WHERE ROWID = ?'''
    curs.execute(cmd, (id,))
    items = curs.fetchall()[0]
    conn.commit()
    conn.close()
    item = InventoryItem
    item.row_id = row[0]
    item.serial_number = row[1]
    item.description = row[2]
    item.location = row[3]
    item.date_arrived = row[4]
    item.date_left = row[5]
    items.append(item)
    # returns a list of tuples
    return items

def add(item):
    conn = sqlite3.connect('inventoryDB.db')
    curs = conn.cursor()
    cmd = '''INSERT INTO FROM tblInventoryItem
     VALUES (
        ?,?,?,?,?
     );'''
    curs.execute(cmd, (item.serial_number, item.description,item.location, item.date_arrived, item.date_left))
    conn.commit()
    conn.close()
    
def update(item):
    conn = sqlite3.connect('inventoryDB.db')
    curs = conn.cursor()
    cmd = '''
    UPDATE tblInventoryItem
    SET
        serial_number = ?,
        description = ?,
        location = ?,
        date_arrived = ?,
        date_left = ?
    WHERE ROWID = ?;

'''
    curs.execute(cmd, (item.serial_number, item.description,item.location, item.date_arrived, item.date_left, item.row_id,))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect('inventoryDB.db')
    curs = conn.cursor()
    cmd = '''
    DELETE FROM tblInventoryItem
    WHERE ROWID = ?
'''
    curs.execute(cmd, (item.serial_number, item.description,item.location, item.date_arrived, item.date_left, item.row_id,))
    conn.commit()
    conn.close()