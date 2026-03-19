from functions import *
#MAIN
# Initial Variables

inventory={
    "name":[],
    "price":[],
    "quantity":[],
    "total_price":[]
    
}

name=""
price=1.1
quantity=0


#I use functions to valid the user input
print("------ Inventory ------")
op=options_inventory()
if op==1:
    keep_add=True
    keep="yes"
    while keep_add:
        print("** Adding Items **")
        name=input("Product Name: ")
        price= verify_product_price()
        quantity=verify_product_quantity()
        total_price=price*quantity
        while keep=="yes":
            keep=input("Do you wnaht to keep adding items YES/NO: ").strip().lower()
            if(keep=="no"):
                keep_add=False
                keep="no"
            elif(keep=="yes"):
                keep="no"
            else:
                keep="yes"
                print("ONLY YES OR NO")
                
elif op==2:
    print()
elif op==3:
    print()
else:
    print()

#Print inventory
print("------------------")
print(f"Product: {name} | Price: {price} | Quantity: {quantity} | Total: {total_price}")