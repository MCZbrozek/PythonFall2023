import sqlite3
import GeoPoint as GeoPoint


def init_db():
    conn = sqlite3.connect('locationsDB.db')
    curs = conn.cursor()

    try:
        curs.execute('''
    CREATE TABLE locationsTbl(
            latitude FLOAT,
            longitude FLOAT,
            city TEXT,
            state TEXT,
            description TEXT,
            distance FLOAT      
                    )                     
    ''')
        
    except sqlite3.OperationalError:
        print('Database was already created.')

        conn.commit
        conn.close()

def get_all():
    conn = sqlite3.connect('locationsDB.db')
    curs = conn.cursor()
    cmd = '''SELECT ROWID, * FROM locationsTbl; '''
    curs.execute(cmd)
    rows = curs.fetchall()
    conn.commit()
    conn.close

    items = []
    for row in rows:
        item = GeoPoint()
        item.row_id = row[0]
        item.lat = row[1]
        item.lon = row[2]
        item.city = row[3]
        item.state = row[4]
        item.description = row[5]
        item.distance = row[6]
        items.append(item)
    return items

def add(item):
    
    conn = sqlite3.connect('locationsDB.db')
    curs = conn.cursor()
    cmd = '''INSERT INTO locationsTbl 
VALUES (?, ?, ?, ?, ?, ?);'''
    curs.execute(cmd, (item.lat, lat.lon, item.cityName, item.state, item.desc, item.distance))
    conn.commit()
    conn.close()