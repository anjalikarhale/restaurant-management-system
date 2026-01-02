import sqlite3
from database import setup_database
setup_database()

conn = sqlite3.connect('restraunt.db')
cursor = conn.cursor()

#printing the menu 

cursor.execute("SELECT * FROM menu_items")
menu = cursor.fetchall()
print("-----MENU-----")
for item in menu:
    print(f"Item:{item[0]},Name:{item[1]},Price:Rs{item[2]}")

#taking order from user
orders = []
while True:
    choice = input("Enter the item id you want to order:(done if finished)")
    if choice.lower()=='done':
        break
    if not choice.isdigit():
        print("Invalid input")
        continue

#check if id exists
    cursor.execute("SELECT * FROM menu_items WHERE id=?",(choice,))
    item = cursor.fetchone()
    if item:
        qty = (input(f"Enter the quantity of {item[1]}: "))
        if not qty.isdigit():
          print("Invalid quantty")
          qty = 1
    
        else:
          qty = int(qty)

          orders.append((item[0],item[1],item[2],qty))
          print(f"Added {qty} of {item[1]} to your order.")
    
    else:
      print("Invalid item id. Please try again")

#generate bill

if orders:
    total=0
    print("-----BILL-----")
    for _id,name,price,qty in orders:
        item_total = price *qty
        total += item_total

        print(f"{name} * {qty} = {item_total}")
        print(f"Total Amount: {total}")
else:
    print("No items ordered")

conn.close()

