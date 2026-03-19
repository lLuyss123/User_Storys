
#Valid the user price
def verify_product_price():
    is_ok=True
    while is_ok:
        try:
            price=float(input("Product Price: "))
            if (price>0):
                is_ok=False
                return price
            else:
                print("Prodcut Price has to be > 0")
        except:
            print("Product Price is not Valid")
        
        
     
     
#Valid the user quantity
def verify_product_quantity():
    is_ok=True
    while is_ok:
        try:
            quantity=int(input("Product Quantity: "))
            if (quantity>0):
                is_ok=False
                return quantity
            else:
                print("Prodcut Quantity has to be > 0")
        except:
            print("Product Quantity is not Valid")

#OP Inventory
def options_inventory():
    is_ok=True
    print("1. Add Product")
    print("2. Show Inventory")
    print("3. Calculate")
    print("4. Exit")
    while is_ok:
        try:
            op=int(input("Selecct an Option: "))
            if op>0 and op<5:
                is_ok=False
                return op
            else:
                print("OPTIONS 1 TO 4 ONLY")
        except:
            print("OPTIONS 1 TO 4 ONLY")
        