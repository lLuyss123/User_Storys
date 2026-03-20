

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



def valid_option_to_contin():
    is_ok=False
    while is_ok==False:
        value=input("Do you want to keep adding items YES/NO: ").lower()
        if value=="no":
            return False
        elif value=="yes":
            return True
        else:
            print("ONLY YES OR NO")
            
            
#def add_to_inventory_list(value,inventory):
    #inventory.append(value)
    
def valid_item_name ():
    is_ok=False
    while is_ok==False:
        item_name=input("Item name: ").strip()
        
        if len(item_name)==0:
            print("Item name cannot be empty")
        else:
            is_ok=True
            return item_name
        
def total_pay(value1,value2):
    total=value1*value2
    return total


def print_inventory(inventory):
    if not inventory:
        print("Inventory is EMPTY")
    else:
        for diccionario in inventory:
            print("-------------------------")
            for key,value in diccionario.items():
                print(key,value)