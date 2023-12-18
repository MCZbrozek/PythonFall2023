# Create and inventory item
sku = ["abc12345", "fds12345"]
description = ["Toaster", "Blender"]
location = ["Shelf 5", "Shelf 3"]
price = ["298.99", "227.14"]
date_arrive_inventory = ["10 oct 2023", "14 oct 2022"]
date_leave_inventory = [None, "11 Nov 2022"]

# Display inventory item information
print("Current Inventory: ")

for i in range(len(sku)):
    print(f"{sku[i]:15} {description[i]:15} {location[i]:15} {price[i]:15} {str(date_arrive_inventory[i]):15} {str(date_leave_inventory[i]):15}")

