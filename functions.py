import csv,os

#OP Inventory
def options_inventory():
    is_ok=True
    print("------ Inventory ------")
    print("1. Add Product")
    print("2. Show Inventory")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Analytics")
    print("7. Save CSV")
    print("8. Upload CSV")
    
    print("9. Exit")
    while is_ok:
        try:
            op=int(input("Selecct an Option: "))
            if op>0 and op<10:
                is_ok=False
                return op
            else:
                print("OPTIONS 1 TO 9 ONLY")
        except:
            print("OPTIONS 1 TO 9 ONLY")




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


#Valid the user option is on the list of op
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
            
#Valid the user name not empty
def valid_item_name ():
    is_ok=False
    while is_ok==False:
        item_name=input("Item name: ").strip()
        
        if len(item_name)==0:
            print("Item name cannot be empty")
        else:
            is_ok=True
            return item_name
        
#Calculate the items total to pay       
def total_pay(value1,value2):
    total=value1*value2
    return total

#Show the inventory that is on a list and inside of the list has dic
def print_inventory(inventory):
    if not inventory:
        print("Inventory is EMPTY")
    else:
        for diccionario in inventory:
            print("-------------------------")
            for key,value in diccionario.items():
                print(key,value)
                
                
                
                
#---------------------------------------------------------------------

def crate_csv(dic):
    archivo_existe = os.path.exists("inventory.csv")
    lista=["Item Name", "Item Price", "Item Quantity", "Total Price"]
    if not archivo_existe:
        with open("inventory.csv","w",newline="") as f:
            csvv= csv.writer(f)
            csvv.writerow(lista)
    
    write_csv(dic)
            
            
            
def write_csv(dic):
    archivo_existe = os.path.exists("inventory.csv")
    lista=["Item Name", "Item Price", "Item Quantity", "Total Price"]
    if archivo_existe:
        with open("inventory.csv","a",newline="") as f:
            csvv= csv.DictWriter(f,fieldnames=lista)
            csvv.writerow(dic)
            
   
   
def print_csv():
    archivo_existe = os.path.exists("inventory.csv")
    if archivo_existe:
        with open("inventory.csv","r" ) as f:
            csvv=csv.DictReader(f)
            for dic in csvv:
                line=""
                for k,v in dic.items():
                    line+= (f"{k}: {v} ")
                print(line)    
    else:
        print("Inventory is Empty")
    
 
         
def search_items(itemname):
    archivo_existe = os.path.exists("inventory.csv")
    if archivo_existe:
        with open("inventory.csv","r" ) as f:
            csvv=csv.DictReader(f)
            find=False
            for dic in csvv:
                line=""
                if dic.get("Item Name")==itemname:
                    find=True
                    for k,v in dic.items():
                        line+= (f"{k}: {v} ")
                    print(line)
            if find ==False:
                print("The Item is NOT into the Inventory")
                    
                         
    

