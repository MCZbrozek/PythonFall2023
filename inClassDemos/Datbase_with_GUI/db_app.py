import tkinter as tk
import tkinter.scrolledtext as st
import DB_repo as db
from InventoryItem import InventoryItem

def add_inventory_item():
    item = InventoryItem()
    item.serial_number = int(serial_entry.get())
    item.description = description_entry.get()
    item.location = location_entry.get()
    item.date_arrived = date_arrived_entry.get()
    item.date_left = date_left_entry.get()
    db.add(item)
    refresh_items()

def remove_item():
    item_id = int(row_id_entry.get())

def refresh_items():
    items_st.delete('1.0','end')
    items = db.get_all()
    for item in items:
        items_st.insert("insert", str(item) + "\n")

# initialize db
db.init_db()

top = tk.Tk()
top.title('Inventory Manager')
top.geometry("900x500")

tk.Label(text = 'Serial number').place(x=10, y=40)
serial_entry = tk.Entry()
serial_entry.place(x=100, y=40)

tk.Label(text = 'description').place(x=10, y=70)
description_entry = tk.Entry()
description_entry.place(x=100, y=70)

tk.Label(text = 'location').place(x=10, y=100)
location_entry = tk.Entry()
location_entry.place(x=100, y=100)

tk.Label(text = 'date_arrived').place(x=10, y=130)
date_arrived_entry = tk.Entry()
date_arrived_entry.place(x=100, y=130)

tk.Label(text = 'date_left').place(x=10, y=160)
date_left_entry = tk.Entry()
date_left_entry.place(x=100, y=160)

tk.Button(text="Add Inventory Item", command = add_inventory_item).place(x=30, y=190)

items_st = st.ScrolledText()
items_st.place(x=10, y= 220)
refresh_items()

tk.Label(text = 'remove item').place(x=10, y=160)
row_id_entry = tk.Entry()
row_id_entry.place(x=400, y=220)

tk.Button(text="Romove Item", command = remove_inventory_item).place(x=400, y=190)

tk.mainloop()
