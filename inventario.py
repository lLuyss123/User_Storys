from functions import *

# Initial Variables

name=""
price=1.1
quantity=0


print("------ Inventory ------")
name=input("Product Name: ")
price= verify_product_price()
quantity=verify_product_quantity()
total_price=price*quantity

print("------------------")
print(f"Product: {name} | Price: {price} | Quantity: {quantity} | Total: {total_price}")